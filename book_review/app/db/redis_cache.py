import redis.asyncio as redis
import json

# Create Redis connection
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Cache: get books from Redis
async def get_books_from_cache():
    cached_books = await r.get("books")
    if cached_books:
        return json.loads(cached_books)
    return None

# Cache: set books in Redis
async def set_books_in_cache(books):
    await r.set("books", json.dumps(books), ex=60)  # expires in 60 sec