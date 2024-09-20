from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient
def get_mongo_client():
    try:
        client = AsyncIOMotorClient(getenv("ATLAS_CONNECTION_URL"))
        yield client['fastapi-mongo']
    finally:
        client.close()