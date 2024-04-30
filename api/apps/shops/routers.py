from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import ShopService,get_shop_service
from . import schema

app = APIRouter(prefix='/api/v1/shops', tags=['shop'])

@app.get('/', summary='список',response_model=List[schema.ShopInfo])
async def list(limit:Optional[int]=50, service:ShopService=Depends(get_shop_service)):
    return await service.get_list(limit)

@app.get('/{id}', summary='один item',response_model=schema.ShopInfo)
async def get_one(id:int, service:ShopService=Depends(get_shop_service)):
    return await service.get_one(id)

@app.post('/', summary='создание', status_code=201)
async def create(data:schema.ShopCreateUpdate, service:ShopService=Depends(get_shop_service)):
    return await service.create(data)

@app.delete('/{id}', summary='удаление')
async def delete(id:int,service:ShopService=Depends(get_shop_service)):
    return await service.delete(id)

@app.put('/', summary='обновление', response_model=schema.ShopInfo)
async def update(data:schema.ShopCreateUpdate, service:ShopService=Depends(get_shop_service)):
    return await service.update(data)