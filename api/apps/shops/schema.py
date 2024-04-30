from pydantic import BaseModel
from typing import Optional

class ShopCreateUpdate(BaseModel):
    id: Optional[int]=None
    name:str
    address:str
    owner_id:int

    class Config:
        orm_mode=True

class ShopInfo(ShopCreateUpdate):
    id:int