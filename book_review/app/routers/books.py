from fastapi import APIRouter, HTTPException
from app.schemas.book import Book, BookIn
from app.db import database
from app.models.book import books
from sqlalchemy import select
from app.db.redis_cache import get_books_from_cache, set_books_in_cache

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[Book])
async def list_books():
    cached_books = await get_books_from_cache()
    if cached_books:
        return cached_books
    query = select(books)
    result = await database.fetch_all(query)
    await set_books_in_cache([dict(row) for row in result])
    return result

@router.post("/", response_model=Book)
async def add_book(book: BookIn):
    query = books.insert().values(**book.dict())
    book_id = await database.execute(query)
    return {**book.dict(), "id": book_id}