from config.settings import Base
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped


class Brands(Base):
    __tablename__='brands'
    id: Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(unique=True)
    

    def __str__(self) -> str:
        return self.name