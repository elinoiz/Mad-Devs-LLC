from pydantic import BaseModel
from fastapi import UploadFile, File, Form
from typing import Optional
from dataclasses import dataclass
from apps.shops.schema import ShopInfo
from apps.brands.schema import BrandInfo


@dataclass
class ProductCreateUpdate:
    name:str=Form(...)
    price:float=Form(...)
    description:str=Form(...)
    image:UploadFile= File(...)
    shop_id:int=Form(...)
    brand_id:int=Form(...)




class ProductInfo(BaseModel):
    id: int
    name:str
    price:float
    description:str
    image: str
    shop:ShopInfo
    brand:BrandInfo

    class Config:
        orm_mode=True