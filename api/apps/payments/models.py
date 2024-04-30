
from typing import Optional
from sqlalchemy import String,ForeignKey, func, text
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from config.settings import Base
from apps.users.models import Users
import enum


class Statuses(enum.Enum):
    inprocess="inprocess"
    success="success"
    denied="denied"



class Payments(Base):
    __tablename__='payments'
    id: Mapped[int]=mapped_column(primary_key=True)
    amount:Mapped[float]
    status:Mapped[Statuses]
    datetime:Mapped[Optional[datetime]]
    
    
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    user:Mapped['Users']=relationship(Users,lazy="joined")


     

    def __str__(self) -> str:
        return self.name