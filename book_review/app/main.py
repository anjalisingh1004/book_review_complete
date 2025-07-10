from fastapi import FastAPI
from app.routers import books, reviews
from app.db.database import database  # ✅ very important

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()  # ✅ from databases.Database

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(books.router)
app.include_router(reviews.router)