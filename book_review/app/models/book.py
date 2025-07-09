from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("author", String),
    Column("published_date", String),
)