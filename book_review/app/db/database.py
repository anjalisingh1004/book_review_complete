import databases
import sqlalchemy


from databases import Database
import sqlalchemy

# ✅ Correct async URL format
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# ✅ Async database object
database = Database(DATABASE_URL)

# ✅ SQLAlchemy engine for creating tables
engine = sqlalchemy.create_engine("sqlite:///./test.db")

from app.models.book import books, metadata
from app.models.review import reviews

metadata.create_all(engine)