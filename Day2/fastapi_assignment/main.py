# test_main.py

from typing import Annotated, List

from Day2.fastapi_assignment.app.models.movies import MovieModel
from Day2.fastapi_assignment.app.models.users import UserModel
from Day2.fastapi_assignment.app.schemas.movies import (
    CreateMovieRequest,
    MovieResponse,
    MovieSearchParams,
    MovieUpdateRequest,
)
from Day2.fastapi_assignment.app.schemas.users import UserData, UserSelect
from fastapi import FastAPI, HTTPException, Path, Query, status

app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.
UserModel.create_dummy()
MovieModel.create_dummy()


@app.get("/users")
async def users():
    user_list = UserModel.all()
    if not user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No user list"
        )
    return user_list


@app.get("/users/select")
async def select_users(
    user: Annotated[UserSelect, Query()]
):  # Query() = ?값으로 읽어온다
    print(user)
    user_filter = UserModel.filter(**user.model_dump())
    return user_filter


@app.get("/users/{user_id}")
async def get(user_id: int = Path(gt=0)):
    user_obj = UserModel.get(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user_obj


@app.get("/movies", response_model=List[MovieResponse], status_code=200)
async def get_movies(query_params: Annotated[MovieSearchParams, Query()]):
    valid_query = {
        key: value
        for key, value in query_params.model_dump().items()
        if value is not None
    }

    if valid_query:
        return MovieModel.filter(**valid_query)

    return MovieModel.all()


@app.get("/movies/{movie_id}", response_model=MovieResponse, status_code=200)
async def get_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    return movie


@app.post("/users")
async def create_user(data: UserData) -> dict[str, int]:
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User data is required",
        )

    user = UserModel.create(**data.model_dump())
    return {"message": user.id}


@app.post(
    "/movies", response_model=MovieResponse, status_code=201
)  # 응답 데이터 구조 강제 통제 및 불필요한 필드 자동 제거
async def create_movie(data: CreateMovieRequest):
    movie = MovieModel.create(**data.model_dump())
    return movie


@app.put("/users/{user_id}")
async def update(
    user_id: int = Path(gt=0),
    user: UserData | None = None,
):
    user_obj = UserModel.get(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User data is required",
        )

    user_obj.update(
        username=user.username,
        age=user.age,
        gender=user.gender,
    )
    return user_obj


@app.patch("/movies/{movie_id}", response_model=MovieResponse, status_code=200)
async def edit_movie(data: MovieUpdateRequest, movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    movie.update(**data.model_dump())
    return movie


@app.delete("/users/{user_id}")
async def delete(
    user_id: int = Path(gt=0), user: UserData | None = None
) -> dict[str, str]:
    user_list = UserModel.get(id=user_id)
    if not user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    user_list.delete()  # id 값으로 정보 하나를 가져 와서 거기에 있는 값(self에 들어감)으로 삭제
    return {"detail": f"User: {user_id}, Successfully Deleted."}


@app.delete("/movies/{movie_id}", status_code=204)
async def delete_movie(movie_id: int = Path(gt=0)):
    movie = MovieModel.get(id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404)
    movie.delete()
    return


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
