from sqlalchemy import String,ForeignKey
from typing import Optional,List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.settings import Base
from apps.users.models import Users

class Shops(Base):
    __tablename__='shops'
    id: Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(unique=True)
    address:Mapped[str]=mapped_column()

    owner_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    owner:Mapped['Users']=relationship(Users, lazy="joined")

    def __str__(self) -> str:
        return self.name