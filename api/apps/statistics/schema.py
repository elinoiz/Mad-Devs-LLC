from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class StatisticsInfo(BaseModel):
    id:int
    brands: int
    payments:int
    products:int
    shops:int
    users:int
    created_at:datetime


    class Config:
        orm_mode=True

class CreateStatistic(BaseModel):
    pass