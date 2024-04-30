from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import StatisticsService, get_statistics_service
from . import schema

app = APIRouter(prefix='/api/v1/statisticss', tags=['statistics'])

@app.get('/', summary='список',response_model=List[schema.StatisticsInfo])
async def list(limit:Optional[int]=50, service:StatisticsService=Depends(get_statistics_service)):
    return await service.get_list(limit)

@app.get('/{id}', summary='один item', response_model=schema.StatisticsInfo)
async def get_one(id:int, service:StatisticsService=Depends(get_statistics_service)):
    return await service.get_one(id)

@app.post('/', summary='создание', status_code=201)
async def create(service:StatisticsService=Depends(get_statistics_service)):
    return await service.create()

@app.delete('/{id}', summary='удаление')
async def delete(id:int,service:StatisticsService=Depends(get_statistics_service)):
    return await service.delete(id)