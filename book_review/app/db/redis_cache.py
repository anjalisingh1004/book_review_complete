import aioredis
import json

redis = None

async def connect():
    global redis
    redis = await aioredis.from_url("redis://localhost", decode_responses=True)

async def disconnect():
    if redis:
        await redis.close()

async def get_books_from_cache():
    try:
        cached = await redis.get("books")
        if cached:
            return json.loads(cached)
    except:
        return None

async def set_books_in_cache(data):
    try:
        await redis.set("books", json.dumps(data), ex=60)
    except:
        pass