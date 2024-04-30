from fastapi import Depends
import os
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from apps.base_repo.base_class import BaseService
from .models import Products
from config.settings import get_session
from utils.save_image import image_add_origin

class ProductService(BaseService[Products]):
    def __init__(self, db_session:Session):
        super(ProductService,self).__init__(Products,db_session)

    async def create(self,product):
        path_folder='static/images/products'
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)
        path_image=image_add_origin(product.image,path_folder)
        async with self.db_session as session:
            new_product=self.table(
                name=product.name,
                price=product.price,
                description=product.description,
                image=path_image,
                shop_id=product.shop_id,
                brand_id=product.brand_id
            )
            session.add(new_product)
            await session.commit()
        return new_product

def get_product_service(db_session:AsyncSession=Depends(get_session)) -> ProductService:
    return ProductService(db_session)
