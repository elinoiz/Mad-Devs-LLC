from typing import Generic, Type, TypeVar, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import Base
from sqlalchemy.future import select
from sqlalchemy import update, delete
from fastapi.responses import JSONResponse



ModelType=TypeVar("ModelType", bound=Base)

class BaseService(Generic[ModelType]):
    def __init__(self,model: Type[ModelType], db_session: AsyncSession):
        self.table=model
        self.db_session=db_session

    async def get_list(self,limit:Optional[int]=None):
        async with self.db_session as session:
            try:
                query= await session.execute(
                select(self.table).limit(limit).order_by(-self.table.id.desc())
            )
                items=query.scalars().all()
                return items
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error: {e}"})
        
    


    async def get_one(self,id):
        async with self.db_session as session:
            try:
                db_item=await session.execute(
                    select(self.table).filter(self.table.id==id)
                )
                db_item=db_item.scalar()
                if not db_item:
                    return JSONResponse(status_code=404, content={"message": "Page not found"})
                return db_item
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error: {e}"})
    
    
    async def create(self,data):
        async with self.db_session as session:
            try:
                item=self.table(**data.dict())
                session.add(item)
                await session.commit()
                return item
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error: {e}"})
    
    async def update(self,data):
        async with self.db_session as session:
            try:

                await session.execute(
                    update(self.table),
                    [data.dict()]
                )
                await session.commit()
                return await self.get_one(data.id)
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error: {e}"})
    

    
    async def delete(self, id):
        async with self.db_session as session:
            try:
                await session.execute(delete(self.table).where(self.table.id == id))
                await session.commit()
                return None
            except Exception as e:
                return JSONResponse(status_code=500, content={"message": f"Error: {e}"})

