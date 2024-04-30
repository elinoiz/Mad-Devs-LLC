from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from apps.base_repo.base_class import BaseService
from .models import Shops
from config.settings import get_session


class ShopService(BaseService[Shops]):
    def __init__(self, db_session:Session):
        super(ShopService,self).__init__(Shops,db_session)

def get_shop_service(db_session:AsyncSession=Depends(get_session)) -> ShopService:
    return ShopService(db_session)
