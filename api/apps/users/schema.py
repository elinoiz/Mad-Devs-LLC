from typing import Optional
from pydantic import BaseModel


class UserCreateUpdate(BaseModel):
    id: Optional[int]=None
    username:str
    email:str
    password_hash:Optional[str]

    class Config:
        orm_mode=True


class UserInfo(UserCreateUpdate):
    id:int
    username:str