from config.settings import Base
from sqlalchemy import String,ForeignKey
from typing import Optional,List
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Users(Base):
    __tablename__='users'
    id: Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String(65),unique=True, index=True)
    email:Mapped[str]=mapped_column(String(120), unique=True,index=True)
    password_hash:Mapped[Optional[str]]=mapped_column(String(120))


    shop=relationship("Shops",back_populates="owner")
    payment=relationship("Payments",back_populates="user")
    

    def __str__(self) -> str:
        return self.name