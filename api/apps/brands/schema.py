from pydantic import BaseModel
from typing import Optional

class BrandCreateUpdate(BaseModel):
    id: Optional[int]=None
    name:str

    class Config:
        orm_mode=True

class BrandInfo(BrandCreateUpdate):
    id:int