# main.py

from typing import Annotated

from fastapi import FastAPI, HTTPException, status, Path, Request, Query

from app.models.users import UserModel
from app.schemas.users import UserData, UserSelect


app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.


@app.api_route("/users", methods=["GET", "POST"])
async def users(request: Request, user: UserData | None = None):
    if request.method == "GET":
        user_list = UserModel.all()
        if not user_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No user list"
            )
        return user_list
    else:
        UserModel.create(user.username, user.age, user.gender)
        return {"message": f"{user.username} Insertion"}


@app.get("/users/select")
async def select_users(
    user: Annotated[UserSelect, Query()]
):  # Query() = ?값으로 읽어온다
    print(user)
    user_filter = UserModel.filter(**user.model_dump())
    return user_filter


@app.get("/users/{user_id}")
async def get(user_id: int = Path(gt=0)):
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return UserModel.get(id=user_id)


@app.put("/users/{user_id}")
async def update(user_id: int = Path(gt=0), user: UserData | None = None):
    user_list = UserModel.get(id=user_id)
    if not user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    user_list.update(
        id=user_id, username=user.username, age=user.age, gender=user.gender
    )
    return user_list


@app.delete("/users/{user_id}")
async def delete(user_id: int = Path(gt=0), user: UserData | None = None):
    user_list = UserModel.get(id=user_id)
    if not user_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    user_list.delete()  # id 값으로 정보 하나를 가져 와서 거기에 있는 값(self에 들어감)으로 삭제
    return {"detail": f"User: {user_id}, Successfully Deleted."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
