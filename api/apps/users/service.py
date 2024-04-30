from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from apps.base_repo.base_class import BaseService
from .models import Users
from config.settings import get_session


class UserService(BaseService[Users]):
    def __init__(self, db_session:Session):
        super(UserService,self).__init__(Users,db_session)

def get_user_service(db_session:AsyncSession=Depends(get_session)) -> UserService:
    return UserService(db_session)
