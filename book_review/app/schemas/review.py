from pydantic import BaseModel

class ReviewIn(BaseModel):
    review_text: str
    rating: int

class Review(ReviewIn):
    id: int
    book_id: int