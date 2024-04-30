
from sqlalchemy import String,ForeignKey
from typing import Optional,List
from sqlalchemy.orm import mapped_column, Mapped, relationship

from config.settings import Base
from apps.brands.models import Brands
from apps.shops.models import Shops

class Products(Base):
    __tablename__='products'
    id: Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(unique=True)
    price:Mapped[float]
    description:Mapped[str]
    image: Mapped[str]
    shop_id:Mapped[int]=mapped_column(ForeignKey("shops.id"))
    brand_id:Mapped[int]=mapped_column(ForeignKey("brands.id"))


    shop:Mapped['Shops']=relationship(Shops,lazy="joined")
    brand:Mapped['Brands']=relationship(Brands,lazy="joined")

     

    def __str__(self) -> str:
        return self.name