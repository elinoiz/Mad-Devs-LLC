from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from apps.base_repo.base_class import BaseService
from .models import Statistics
from config.settings import get_session
from sqlalchemy import func, select
from apps.users.models import Users
from apps.shops.models import Shops
from apps.brands.models import Brands
from apps.payments.models import Payments
from apps.products.models import Products


class StatisticsService(BaseService[Statistics]):
    def __init__(self, db_session: Session):
        super().__init__(Statistics, db_session)

    async def create(self):
        async with self.db_session as session:
            brands_count = await session.execute(select(func.count(Brands.id)))
            brands_count = brands_count.scalar()
            
            payments_count = await session.execute(select(func.count(Payments.id)))
            payments_count = payments_count.scalar()
            
            products_count = await session.execute(select(func.count(Products.id)))
            products_count = products_count.scalar()
            
            shops_count = await session.execute(select(func.count(Shops.id)))
            shops_count =  shops_count.scalar()
            
            users_count = await session.execute(select(func.count(Users.id)))
            users_count = users_count.scalar()
            
            item = self.table(
                brands=brands_count,
                payments=payments_count,
                products=products_count,
                shops=shops_count,
                users=users_count,
            )
            session.add(item)
            await session.commit()
        return item

def get_statistics_service(db_session:AsyncSession=Depends(get_session)) -> StatisticsService:
    return StatisticsService(db_session)
