from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PaymentCreateUpdate(BaseModel):
    id: Optional[int]=None
    amount:float
    status:str
    datetime:datetime
    user_id:int

    class Config:
        orm_mode=True


class PaymentInfo(PaymentCreateUpdate):
    id:int
    