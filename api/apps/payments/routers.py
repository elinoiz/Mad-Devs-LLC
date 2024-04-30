from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import PaymentService, get_payment_service
from . import schema

app = APIRouter(prefix='/api/v1/payments', tags=['payment'])

@app.get('/', summary='список',response_model=List[schema.PaymentInfo])
async def list(limit:Optional[int]=50, service:PaymentService=Depends(get_payment_service)):
    return await service.get_list(limit)

@app.get('/{id}', summary='один item', response_model=schema.PaymentInfo)
async def get_one(id:int, service:PaymentService=Depends(get_payment_service)):
    return await service.get_one(id)

@app.post('/', summary='создание', status_code=201)
async def create(data:schema.PaymentCreateUpdate, service:PaymentService=Depends(get_payment_service)):
    return await service.create(data)

@app.delete('/{id}', summary='удаление')
async def delete(id:int,service:PaymentService=Depends(get_payment_service)):
    return await service.delete(id)

@app.put('/', summary='обновление', response_model=schema.PaymentInfo)
async def update(data:schema.PaymentCreateUpdate, service:PaymentService=Depends(get_payment_service)):
    return await service.update(data)