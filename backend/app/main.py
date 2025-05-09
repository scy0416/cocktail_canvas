from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Query
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

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
def login_kakao_callback(code: str = Query(None)):
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
    user_nickname = user_info_json.get("properties").get("nickname")
    if not user_nickname:
        raise HTTPException(status_code=500, detail="카카오 사용자 정보를 받아오지 못했습니다.")
    
    return {"message": "카카오 사용자 정보를 받아왔습니다.", "user_nickname": user_nickname}