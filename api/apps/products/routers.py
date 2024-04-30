from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import ProductService, get_product_service
from . import schema

app = APIRouter(prefix='/api/v1/products', tags=['product'])

@app.get('/', summary='список',response_model=List[schema.ProductInfo])
async def list(limit:Optional[int]=50, service:ProductService=Depends(get_product_service)):
    return await service.get_list(limit)

@app.get('/{id}', summary='один item', response_model=schema.ProductInfo)
async def get_one(id:int, service:ProductService=Depends(get_product_service)):
    return await service.get_one(id)

@app.post('/', summary='создание', status_code=201)
async def create(data:schema.ProductCreateUpdate= Depends(), service:ProductService=Depends(get_product_service)):
    return await service.create(data)

@app.delete('/{id}', summary='удаление')
async def delete(id:int,service:ProductService=Depends(get_product_service)):
    return await service.delete(id)

@app.put('/', summary='обновление', response_model=schema.ProductInfo)
async def update(data:schema.ProductCreateUpdate, service:ProductService=Depends(get_product_service)):
    return await service.update(data)