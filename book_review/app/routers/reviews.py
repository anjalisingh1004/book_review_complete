from fastapi import APIRouter, HTTPException
from app.schemas.review import Review, ReviewIn
from app.db import database
from app.models.review import reviews
from sqlalchemy import select

router = APIRouter(prefix="/books", tags=["Reviews"])

@router.get("/{book_id}/reviews", response_model=list[Review])
async def get_reviews(book_id: int):
    query = select(reviews).where(reviews.c.book_id == book_id)
    return await database.fetch_all(query)

@router.post("/{book_id}/reviews", response_model=Review)
async def add_review(book_id: int, review: ReviewIn):
    query = reviews.insert().values(book_id=book_id, **review.dict())
    review_id = await database.execute(query)
    return {**review.dict(), "book_id": book_id, "id": review_id}