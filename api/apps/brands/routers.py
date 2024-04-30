from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import BrandService, get_brand_service
from . import schema

app = APIRouter(prefix='/api/v1/brands', tags=['brand'])

@app.get('/', summary='список',response_model=List[schema.BrandInfo])
async def list(limit:Optional[int]=50, service:BrandService=Depends(get_brand_service)):
    return await service.get_list(limit)

@app.get('/{id}', summary='один item', response_model=schema.BrandInfo)
async def get_one(id:int, service:BrandService=Depends(get_brand_service)):
    return await service.get_one(id)

@app.post('/', summary='создание', status_code=201)
async def create(data:schema.BrandCreateUpdate, service:BrandService=Depends(get_brand_service)):
    return await service.create(data)

@app.delete('/{id}', summary='удаление')
async def delete(id:int,service:BrandService=Depends(get_brand_service)):
    return await service.delete(id)

@app.put('/', summary='обновление', response_model=schema.BrandInfo)
async def update(data:schema.BrandCreateUpdate, service:BrandService=Depends(get_brand_service)):
    return await service.update(data)