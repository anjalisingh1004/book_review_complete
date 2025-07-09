import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/books")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_post_book():
    payload = {"title": "Test Book", "author": "Test Author", "published_date": "2024"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/books", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"