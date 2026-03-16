# main.py
from typing import Annotated

from fastapi import FastAPI, HTTPException,status,Path,Query

from app.models.users import UserModel

from app.schemas.users import CreatUser,UpdateUser,UserFilter

app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.

# 1. 유저 생성 API 라우터 작성
@app.post("/users")
async def create_users(user_info: CreatUser):
    user = UserModel(**user_info.model_dump())
    return user.id

# 2. 모든 유저 정보 가져오는 API 라우터 작성
## 유저가 1명도 없을 경우 에럴 발생
@app.get("/users")
async def get_users():
    users = UserModel.all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return users

## 3~5 번 공통 조건
## 경로 매개 변수로 전달
## 검증된 user_id를 통해 UserModel객체를 가져온뒤 반환하는 API 라우터 작성
## user_id 검증의 경우 Path객체를 사용
## 해당 유저가 없을 경우 404에러 발생


# 3.유저 정보를 가져오는 API 작성
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(gt=0) ):
    user = UserModel.get(id = user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

# 4.유저 정보를 수정하는 API 라우터 작성
@app.put("/users/{user_id}")
async def update_user(user_info:UpdateUser,user_id: int = Path(gt=0)):
    user = UserModel.get(id = user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user.update(UpdateUser(**user_info.model_dump()))

    return user

# 5. 유저를 삭제하는 API 라우터 작성
@app.delete("/users/{user_id}")
async def delete_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id = user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user.delete()
    return {'detail':f"User:{user_id},Successfully deleted"}
# 6. 유저 정보를 검색하는 API라우터 작성
@app.get("/users/filter")
async def get_user_filter(q:Annotated[UserFilter,Query()]):
    filter_data =q.model_dump(exclude_none=True)
    if not filter_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # filter_data는 객체상태(딕트 형태) 데이터 이용하려면 언패키징 필요
    user_filter_dict={key:value for key,value in filter_data.items()}
    result=UserModel.filter(**user_filter_dict)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result







if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)