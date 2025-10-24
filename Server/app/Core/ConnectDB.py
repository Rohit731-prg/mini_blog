from motor.motor_asyncio import AsyncIOMotorClient
from app.Core.Config import settings

url = settings.DB_URL
client = AsyncIOMotorClient(url)

db = client["SnapBoard"]

collection_user = db["users"]
collection_post = db["posts"]