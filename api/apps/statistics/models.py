from config.settings import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.sql import func
from datetime import datetime


class Statistics(Base):
    __tablename__='statistics'
    id: Mapped[int]=mapped_column(primary_key=True)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
   
    brands = Column(Integer, ForeignKey('brands.id'))
    payments = Column(Integer, ForeignKey('payments.id'))
    products = Column(Integer, ForeignKey('products.id'))
    shops = Column(Integer, ForeignKey('shops.id'))
    users = Column(Integer, ForeignKey('users.id'))

    brands_rel = relationship("Brands")
    payments_rel = relationship("Payments")
    products_rel = relationship("Products")
    shops_rel = relationship("Shops")
    users_rel = relationship("Users")
    
    

def __repr__(self):
        return f"<Statistics(brands={self.brands}, payments={self.payments}, products={self.products}, shops={self.shops}, users={self.users}, created_at={self.created_at})>"