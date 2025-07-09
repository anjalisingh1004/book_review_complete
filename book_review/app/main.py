from fastapi import FastAPI
from app.routers import books, reviews
from app.db import database, redis_cache

app = FastAPI()

app.include_router(books.router)
app.include_router(reviews.router)

@app.on_event("startup")
async def startup():
    await database.connect()
    await redis_cache.connect()

@app.on_event("shutdown")
async def shutdown():
    await redis_cache.disconnect()
    await database.disconnect()