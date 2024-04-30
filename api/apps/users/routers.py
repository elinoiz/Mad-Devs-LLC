from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import UserService, get_user_service
from . import schema

app = APIRouter(prefix='/api/v1/users', tags=['user'])

@app.get('/', summary='список',response_model=List[schema.UserInfo])
async def list(limit:Optional[int]=50, service:UserService=Depends(get_user_service)):
    return await service.get_list(limit)

@app.get('/{id}', summary='один item', response_model=schema.UserInfo)
async def get_one(id:int, service:UserService=Depends(get_user_service)):
    return await service.get_one(id)

@app.post('/', summary='создание', status_code=201)
async def create(data:schema.UserCreateUpdate, service:UserService=Depends(get_user_service)):
    return await service.create(data)

@app.delete('/{id}', summary='удаление')
async def delete(id:int,service:UserService=Depends(get_user_service)):
    return await service.delete(id)

@app.put('/', summary='обновление', response_model=schema.UserInfo)
async def update(data:schema.UserCreateUpdate, service:UserService=Depends(get_user_service)):
    return await service.update(data)