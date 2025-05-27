from fastapi import FastAPI, Cookie
from fastapi.responses import RedirectResponse
from fastapi import Query, Depends
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import requests
import os
from datetime import datetime, timedelta
from fastapi.responses import Response
from fastapi import Request
import jwt
from app.models import *
import random
from random import Random
from datetime import datetime, date
from fastapi import File, UploadFile, Form, Path
from typing import List
import aiofiles
import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

"""
환경설정 영역 시작
"""

# 환경변수 로드
load_dotenv()

# 서버 객체 생성
app = FastAPI()

llm = OllamaLLM(model="gemma3:4b", base_url=os.getenv("BASE_URL"))

# 데이터베이스 연결 생성
SECRET_KEY = "cocktail_canvas"
ALGORITHM = "HS256"
DATABASE_URL = f"mysql+pymysql://root:{os.getenv('MYSQL_ROOT_PASSWORD')}@mysql:3306/cocktail_canvas"
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
환경설정 영역 끝
"""

"""
의존성 영역 시작
"""

# 데이터베이스 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 액세스 토큰 발행 함수
def create_access_token(data):
    to_encode = data.as_dict()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 리프레시 토큰 발행 함수
def create_refresh_token(data):
    to_encode = data.as_dict()
    expire = datetime.utcnow() + timedelta(days=90)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 토큰 검증 함수
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰이 만료되었습니다.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")

"""
의존성 영역 끝
"""

"""
라우팅 영역 시작
"""

@app.get("/api/test")
async def test():
    return {"message": "api_test"}

@app.get("/api/login/kakao")
def login_kakao():
    """
    카카오 인증 페이지로 리다이렉트한다.
    """
    kakao_auth_url = (
        "https://kauth.kakao.com/oauth/authorize"
        f"?client_id={os.getenv('KAKAO_CLIENT_ID')}"
        f"&redirect_uri={os.getenv('KAKAO_REDIRECT_URI')}"
        "&response_type=code"
        "&prompt=select_account"
    )
    return RedirectResponse(kakao_auth_url)

@app.get("/api/login/kakao/callback")
async def login_kakao_callback(code: str = Query(None), db: Session = Depends(get_db)):
    """
    카카오에서 인가 코드를 받아서 access token 및 사용자 정보를 요청한다.
    """
    if not code:
        raise HTTPException(status_code=400, detail="인가 코드가 없습니다.")
    
    # access token 요청
    data = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("KAKAO_CLIENT_ID"),
        "redirect_uri": os.getenv("KAKAO_REDIRECT_URI"),
        "code": code
    }

    token_response = requests.post("https://kauth.kakao.com/oauth/token", data=data)
    if token_response.status_code != 200:
        raise HTTPException(status_code=500, detail="카카오 인가 코드를 받아서 access token 및 사용자 정보를 요청하는 데 실패했습니다.")
    
    token_json = token_response.json()
    access_token = token_json.get("access_token")
    if not access_token:
        raise HTTPException(status_code=500, detail="access token을 받아오지 못했습니다.")
    
    # access token을 사용해 사용자 정보 요청
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    user_info_response = requests.get("https://kapi.kakao.com/v2/user/me", headers=headers)
    if user_info_response.status_code != 200:
        raise HTTPException(status_code=500, detail="카카오 사용자 정보를 받아오지 못했습니다.")
    
    user_info_json = user_info_response.json()
    kakao_id = user_info_json.get("id")
    nickname = user_info_json.get("properties").get("nickname")

    user = db.query(User).filter(User.kakao_id == kakao_id).first()
    if not user:
        user = User(kakao_id=kakao_id, name=nickname)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    user = db.query(User).filter(User.kakao_id == kakao_id).first()
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)

    response = RedirectResponse(url="/#/", status_code=302)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        max_age=60*60*24*7
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        max_age=60*60*24*7
    )
    
    return response

@app.post("/api/auth/verify")
def verify(response: Response, access_token: str = Cookie(None), refresh_token: str = Cookie(None), db: Session = Depends(get_db)):
    """
    1) access_token 검증
    2) refresh_token 검증
    3) refresh_token으로 access_token 재발행
    4) access_token과 refresh_token을 쿠키에 저장
    5) 쿠키를 응답에 포함
    """
    # 1) access_token 검증
    if not access_token:
        raise HTTPException(status_code=401, detail="토큰이 없습니다. 로그인 해주세요.")
    
    # 2) access_token 검증
    try:
        payload = verify_token(access_token)
        return {"message": "access token valid", "user": payload}
    except HTTPException as e:
        if e.status_code == 401 and "만료" in e.detail:
            if not refresh_token:
                raise HTTPException(status_code=401, detail="리프레시 토큰이 없습니다. 다시 로그인하세요.")
            try:
                refresh_payload = verify_token(refresh_token)
            except HTTPException:
                raise HTTPException(status_code=401, detail="리프레시 토큰이 만료되었습니다. 다시 로그인하세요.")
            user = db.query(User).filter(User.id == refresh_payload.get("id")).first()
            if not user:
                raise HTTPException(status_code=401, detail="유효하지 않은 사용자입니다.")
            new_access_token = create_access_token(user)
            new_refresh_token = create_refresh_token(user)

            cookie_opts = {
                "httponly": True,
                "secure": True,
            }
            response.set_cookie(key="access_token", value=new_access_token, **cookie_opts)
            response.set_cookie(key="refresh_token", value=new_refresh_token, **cookie_opts)

            return {"message": "tokens refreshed", "user": refresh_payload}
        raise

@app.post("/api/logout")
def logout(response: Response):
    """
    1) access_token 삭제
    2) refresh_token 삭제
    """
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "logout successful"}

@app.get("/api/cocktails")
def get_cocktails(db: Session = Depends(get_db)):
    """
    칵테일 리스트를 반환한다.
    """
    print("칵테일 리스트 테스트")
    cocktails = db.query(Cocktail).all()
    return cocktails

@app.get("/api/recommend/random")
def recommend_random_cocktail(db: Session = Depends(get_db)):
    """
    랜덤 추천 칵테일 리스트를 반환한다.
    """
    now = str(datetime.now())
    random.seed(now)
    cocktails = db.query(Cocktail).all()
    random_cocktails = random.sample(cocktails, 4)
    result = []
    for cocktail in random_cocktails:
        tmp = {}
        tmp["name"] = cocktail.name
        tmp["description"] = cocktail.description
        tmp["alcohol"] = cocktail.alcohol
        tmp["image_url"] = cocktail.image_url
        tmp["id"] = cocktail.id
        tmp["tags"] = []
        for tag in cocktail.tags:
            tmp["tags"].append(tag.tag)
        result.append(tmp)
    return result

@app.get("/api/recommend/daily")
def recommend_daily_cocktail(db: Session = Depends(get_db)):
    """
    일일 추천 칵테일 리스트를 반환한다.
    """
    today = str(date.today())
    rng = Random(today)
    cocktails = db.query(Cocktail).all()
    random_cocktails = rng.sample(cocktails, 4)
    result = []
    for cocktail in random_cocktails:
        tmp = {}
        tmp["name"] = cocktail.name
        tmp["description"] = cocktail.description
        tmp["alcohol"] = cocktail.alcohol
        tmp["image_url"] = cocktail.image_url
        tmp["id"] = cocktail.id
        tmp["tags"] = []
        for tag in cocktail.tags:
            tmp["tags"].append(tag.tag)
        result.append(tmp)
    return result

@app.get("/api/cocktail/{id}")
def get_cocktail(id: int, db: Session = Depends(get_db)):
    """
    칵테일 정보를 반환한다.
    """
    cocktail = db.query(Cocktail).filter(Cocktail.id == id).first()
    if not cocktail:
        raise HTTPException(status_code=404, detail="해당 칵테일을 찾을 수 없습니다.")
    result = {}
    result["name"] = cocktail.name
    result["description"] = cocktail.description
    result["alcohol"] = cocktail.alcohol
    result["image_url"] = cocktail.image_url
    result["user_review"] = cocktail.user_review
    result["tags"] = []
    for tag in cocktail.tags:
        result["tags"].append(tag.tag)
    result["recipe_ingredients"] = []
    for recipe_ingredient in cocktail.recipe_ingredients:
        result["recipe_ingredients"].append({
            "name": recipe_ingredient.ingredient.name,
            "tag": recipe_ingredient.ingredient.tag,
            "amount": recipe_ingredient.amount
        })
    result["recipes"] = []
    for recipe in cocktail.recipes:
        result["recipes"].append(recipe.recipe)
    return result

@app.get("/api/iba-cocktail")
def get_ibacocktails(sort: str = Query("name-asc"), db: Session = Depends(get_db)):
    """
    IBA 칵테일 리스트를 반환한다.
    """
    cocktails = db.query(Cocktail).filter(Cocktail.id <= 20)
    match sort:
        case "name-asc":
            cocktails = cocktails.order_by(Cocktail.name.asc())
        case "name-desc":
            cocktails = cocktails.order_by(Cocktail.name.desc())
        case "alcoholic-asc":
            cocktails = cocktails.order_by(Cocktail.alcohol.asc())
        case "alcoholic-desc":
            cocktails = cocktails.order_by(Cocktail.alcohol.desc())
    cocktails = cocktails.all()
    result = []
    for cocktail in cocktails:
        tmp = {}
        tmp["name"] = cocktail.name
        tmp["description"] = cocktail.description
        tmp["alcohol"] = cocktail.alcohol
        tmp["image_url"] = cocktail.image_url
        tmp["id"] = cocktail.id
        tmp["tags"] = []
        for tag in cocktail.tags:
            tmp["tags"].append(tag.tag)
        result.append(tmp)
    return result

@app.get("/api/custom-cocktail")
def get_customcocktails(sort: str = Query("name-asc"), db: Session = Depends(get_db)):
    """
    사용자가 만든 칵테일 리스트를 반환한다.
    """
    cocktails = db.query(Cocktail).filter(Cocktail.id > 20)
    match sort:
        case "name-asc":
            cocktails = cocktails.order_by(Cocktail.name.asc())
        case "name-desc":
            cocktails = cocktails.order_by(Cocktail.name.desc())
        case "alcoholic-asc":
            cocktails = cocktails.order_by(Cocktail.alcohol.asc())
        case "alcoholic-desc":
            cocktails = cocktails.order_by(Cocktail.alcohol.desc())
    cocktails = cocktails.all()
    result = []
    for cocktail in cocktails:
        tmp = {}
        tmp["name"] = cocktail.name
        tmp["description"] = cocktail.description
        tmp["alcohol"] = cocktail.alcohol
        tmp["image_url"] = cocktail.image_url
        tmp["id"] = cocktail.id
        tmp["tags"] = []
        for tag in cocktail.tags:
            tmp["tags"].append(tag.tag)
        result.append(tmp)
    return result

@app.post("/api/user-cocktail")
def get_usercocktails(
    response: Response,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
):
    """
    사용자가 만든 칵테일 리스트를 반환한다.
    """
    cocktails = db.query(Cocktail).filter(Cocktail.user_id == user['user']['id']).all()
    result = []
    for cocktail in cocktails:
        tmp = {}
        tmp["name"] = cocktail.name
        tmp["description"] = cocktail.description
        tmp["alcohol"] = cocktail.alcohol
        tmp["image_url"] = cocktail.image_url
        tmp["id"] = cocktail.id
        tmp["tags"] = []
        for tag in cocktail.tags:
            tmp["tags"].append(tag.tag)
        result.append(tmp)
    return result

@app.post("/api/cocktail/delete/{cocktail_id}")
def delete_cocktail(
    response: Response,
    cocktail_id: int,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
):
    """
    사용자가 만든 칵테일을 삭제한다.
    """
    cocktail = db.query(Cocktail).filter(Cocktail.id == cocktail_id).first()
    if not cocktail:
        raise HTTPException(status_code=404, detail="해당 칵테일을 찾을 수 없습니다.")
    if cocktail.user_id != user['user']['id']:
        raise HTTPException(status_code=403, detail="해당 칵테일을 삭제할 수 없습니다.")
    db.delete(cocktail)
    db.commit()
    return {"message": "cocktail deleted"}

@app.post("/api/custom-cocktail/register")
async def create_custom_cocktail(
    response: Response,
    request: Request,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
    name: str = Form(...),
    description: str = Form(...),
    ingredients: List[str] = Form(...),
    ingredient_amounts: List[str] = Form(...),
    recipes: List[str] = Form(...),
    tags: List[str] = Form(...),
    image: UploadFile = File(...),
    alcohol: float = Form(...),
):
    """
    사용자가 만든 칵테일을 등록한다.
    """

    ingredients = ingredients[0].split(',')
    ingredient_amounts = ingredient_amounts[0].split(',')
    recipes = recipes[0].split(',')
    tags = tags[0].split(',')

    # 칵테일 생성
    cocktail = Cocktail(
        user_id=user['user']['id'],
        name=name,
        description=description,
        alcohol=alcohol,
        user_review="-",
        image_url=""
    )
    db.add(cocktail)
    db.commit()
    db.refresh(cocktail)

    # 이미지 저장
    async with aiofiles.open(f"./images/{cocktail.id}_{name}.png", "wb") as out_file:
        while content := await image.read(1024):
            await out_file.write(content)
    
    cocktail.image_url = f"{cocktail.id}_{name}.png"
    db.commit()

    # 태그 저장
    for tag in tags:
        tmp = CocktailTag(cocktail_id=cocktail.id, tag=tag)
        db.add(tmp)
    db.commit()

    # 재료 등록
    for ingredient, ingredient_amount in zip(ingredients, ingredient_amounts):
        tmp = Ingredient(name=ingredient)
        db.add(tmp)
        db.commit()
        db.refresh(tmp)

        tmp2 = RecipeIngredient(cocktail_id=cocktail.id, ingredient_id=tmp.id, amount=ingredient_amount)
        db.add(tmp2)
        db.commit()
    
    # 레시피 저장
    for recipe in recipes:
        tmp = Recipe(cocktail_id=cocktail.id, recipe=recipe)
        db.add(tmp)
        db.commit()
    
    return {"message": "cocktail registered"}

@app.get("/api/search-cocktail")
def get_searchcocktails(sort: str = Query("name-asc"), q: str = Query(...), db: Session = Depends(get_db)):
    """
    검색된 칵테일 리스트를 반환한다.
    """
    cocktails = db.query(Cocktail).filter(Cocktail.name.contains(q))
    match sort:
        case "name-asc":
            cocktails = cocktails.order_by(Cocktail.name.asc())
        case "name-desc":
            cocktails = cocktails.order_by(Cocktail.name.desc())
        case "alcoholic-asc":
            cocktails = cocktails.order_by(Cocktail.alcohol.asc())
        case "alcoholic-desc":
            cocktails = cocktails.order_by(Cocktail.alcohol.desc())
    cocktails = cocktails.all()
    result = []
    for cocktail in cocktails:
        tmp = {}
        tmp["name"] = cocktail.name
        tmp["description"] = cocktail.description
        tmp["alcohol"] = cocktail.alcohol
        tmp["image_url"] = cocktail.image_url
        tmp["id"] = cocktail.id
        tmp["tags"] = []
        for tag in cocktail.tags:
            tmp["tags"].append(tag.tag)
        result.append(tmp)
    return result

@app.get("/api/cocktail/{cocktail_id}/review")
def get_cocktailreview(cocktail_id: int, db: Session = Depends(get_db)):
    """
    칵테일 리뷰 리스트를 반환한다.
    """
    reviews = db.query(Review).filter(Review.cocktail_id == cocktail_id).all()
    result = []
    for review in reviews:
        tmp = {}
        tmp["name"] = review.user.name
        tmp["date"] = review.review_date
        tmp["rating"] = review.rating
        tmp["review_json"] = review.comment
        result.append(tmp)
    return result

@app.post("/api/cocktail/{cocktail_id}/review/my")
def get_myreview(
    response: Response,
    request: Request,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
    cocktail_id: int = Path(...)
):
    """
    사용자의 리뷰를 반환한다.
    """
    review = db.query(Review).filter(Review.user_id == user['user']['id'], Review.cocktail_id == cocktail_id).first()
    if not review:
        #raise HTTPException(status_code=404, detail="해당 리뷰를 찾을 수 없습니다.")
        return None
    review_dict = {
        "name": review.user.name,
        "date": review.review_date,
        "rating": review.rating,
        "review_json": review.comment
    }
    return review_dict

@app.post("/api/cocktail/{cocktail_id}/review")
async def post_review(
    response: Response,
    request: Request,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
    cocktail_id: int = Path(...),
):
    """
    리뷰를 작성한다.
    """
    request_json = await request.json()
    rating = request_json['rating']
    review = request_json['review']

    # 맛, 느낌, 분위기, 안주 추출
    parser = JsonOutputParser(return_id=True)

    format_instructions = """다음 JSON 형식을 지켜주세요:
    {
    "taste": "맛 설명, 맛 설명이 없다면 '-'",
    "feeling": "느낌 설명, 느낌 설명이 없다면 '-'",
    "atmosphere": "분위기 설명, 분위기 설명이 없다면 '-'",
    "appetizer": "안주 설명, 안주 설명이 없다면 '-'"
    }
    """
    prompt = PromptTemplate(
        template="리뷰 내용을 배탕으로 다음 형식으로 분리해줘.\n{format_instructions}\n리뷰: {review}",
        input_variables=["review", "format_instructions"]
    )

    chain = prompt | llm | parser

    result = chain.invoke({"review": review, "format_instructions": format_instructions})
    
    review_dict = {
        "review": review,
        "taste": result["taste"],
        "feeling": result["feeling"],
        "atmosphere": result["atmosphere"],
        "appetizer": result["appetizer"]
    }
    review = Review(
        user_id=user['user']['id'],
        cocktail_id=cocktail_id,
        rating=rating,
        comment=json.dumps(review_dict, ensure_ascii=False)
    )
    db.add(review)
    db.commit()
    return

@app.post("/api/cocktail/{cocktail_id}/review/delete")
def delete_review(
    response: Response,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
    cocktail_id: int = Path(...)
):
    """
    리뷰를 삭제한다.
    """
    review = db.query(Review).filter(Review.user_id == user['user']['id'], Review.cocktail_id == cocktail_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="해당 리뷰를 찾을 수 없습니다.")
    db.delete(review)
    db.commit()
    return

@app.post("/api/cocktail/{cocktail_id}/review/update")
async def update_review(
    response: Response,
    request: Request,
    user: dict = Depends(verify),
    db: Session = Depends(get_db),
    cocktail_id: int = Path(...),
):
    """
    리뷰를 수정한다.
    """
    request_json = await request.json()
    rating = request_json['rating']
    review = request_json['review']

    # 맛, 느낌, 분위기, 안주 추출
    parser = JsonOutputParser(return_id=True)

    format_instructions = """다음 JSON 형식을 지켜주세요:
    {
    "taste": "맛 설명, 맛 설명이 없다면 '-'",
    "feeling": "느낌 설명, 느낌 설명이 없다면 '-'",
    "atmosphere": "분위기 설명, 분위기 설명이 없다면 '-'",
    "appetizer": "안주 설명, 안주 설명이 없다면 '-'"
    }
    """
    prompt = PromptTemplate(
        template="리뷰 내용을 배탕으로 다음 형식으로 분리해줘.\n{format_instructions}\n리뷰: {review}",
        input_variables=["review", "format_instructions"]
    )

    chain = prompt | llm | parser

    result = chain.invoke({"review": review, "format_instructions": format_instructions})
    review_dict = {
        "review": review,
        "taste": result["taste"],
        "feeling": result["feeling"],
        "atmosphere": result["atmosphere"],
        "appetizer": result["appetizer"]
    }
    review = db.query(Review).filter(Review.user_id == user['user']['id'], Review.cocktail_id == cocktail_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="해당 리뷰를 찾을 수 없습니다.")
    review.rating = rating
    review.comment = json.dumps(review_dict, ensure_ascii=False)
    db.commit()
    return