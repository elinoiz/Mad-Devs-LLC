from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from apps.base_repo.base_class import BaseService
from .models import Payments
from config.settings import get_session


class PaymentService(BaseService[Payments]):
    def __init__(self, db_session:Session):
        super(PaymentService,self).__init__(Payments,db_session)

def get_payment_service(db_session:AsyncSession=Depends(get_session)) -> PaymentService:
    return PaymentService(db_session)
