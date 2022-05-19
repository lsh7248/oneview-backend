import uvicorn
from fastapi import FastAPI
from routers.api.api_v1.api import api_v1_router
from starlette.middleware.cors import CORSMiddleware

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI()
    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 라우터 정의
    app.include_router(api_v1_router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)