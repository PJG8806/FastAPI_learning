# test_main.py


from Day5.fastapi_assignment.app.models.movies import MovieModel
from Day5.fastapi_assignment.app.models.users import UserModel
from Day5.fastapi_assignment.app.routers.movies import movie_router
from Day5.fastapi_assignment.app.routers.users import user_router
from fastapi import FastAPI
from query.app import initialize_tortoise

app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.
MovieModel.create_dummy()

app.include_router(user_router)
app.include_router(movie_router)

initialize_tortoise(app=app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
