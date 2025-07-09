import pytest
from httpx import AsyncClient
from app.main import app
from app.db.redis_cache import redis

@pytest.mark.asyncio
async def test_cache_miss_then_db_fetch():
    if redis:
        await redis.delete("books")
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/books")
    assert response.status_code == 200