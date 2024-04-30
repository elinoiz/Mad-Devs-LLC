from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config.settings import Base, engine
from apps.brands.routers import app as brand_app
from apps.shops.routers import app as shop_app
from apps.products.routers import app as product_app
from apps.users.routers import app as user_app
from apps.payments.routers import app as payment_app
from apps.statistics.routers import app as statistic_app

app=FastAPI()

app.mount('/static', StaticFiles(directory='static'),name='static')
origin_cors=['*']

app.add_middleware(
CORSMiddleware,
allow_origins=origin_cors, 
allow_credentials=True,
allow_methods=["*"], 
allow_headers=["*"], 
)

@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(shop_app)
app.include_router(brand_app)
app.include_router(product_app)
app.include_router(user_app)
app.include_router(payment_app)
app.include_router(statistic_app)


