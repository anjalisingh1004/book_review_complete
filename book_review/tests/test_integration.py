import pytest
from httpx import AsyncClient
from app.main import app
from app.db.redis_cache import redis

@pytest.mark.asyncio
async def test_cache_miss_then_db_fetch():
    """
    This test checks if the app correctly fetches books from the DB
    when Redis cache is empty (cache miss).
    """
    # ✅ Step 1: Clear cache
    if redis:
        await redis.delete("books")

    # ✅ Step 2: Make GET request to /books/
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/books/")

    # ✅ Step 3: Validate response
    assert response.status_code == 200
    assert isinstance(response.json(), list)
