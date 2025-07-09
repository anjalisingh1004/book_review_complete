from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, Index

metadata = MetaData()

reviews = Table(
    "reviews",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("review_text", String),
    Column("rating", Integer),
)

Index("ix_reviews_book_id", reviews.c.book_id)