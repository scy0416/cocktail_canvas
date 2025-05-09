from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Query, Depends
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import requests
import os
from datetime import datetime, timedelta
import jwt
from app.models import *

"""
환경설정 영역 시작
"""

# 환경변수 로드
load_dotenv()

# 서버 객체 생성
app = FastAPI()

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

@app.get("/api/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

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