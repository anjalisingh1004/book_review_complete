import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)

from app.models.book import books, metadata
from app.models.review import reviews

metadata.create_all(engine)