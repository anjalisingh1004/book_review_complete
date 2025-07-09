from pydantic import BaseModel

class BookIn(BaseModel):
    title: str
    author: str
    published_date: str

class Book(BookIn):
    id: int