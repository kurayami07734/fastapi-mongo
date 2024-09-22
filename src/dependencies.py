from os import getenv
from typing import Generator

from odmantic import AIOEngine

from motor.motor_asyncio import AsyncIOMotorClient

def db_engine() -> Generator[AIOEngine, None, None]:
    try:
        client = AsyncIOMotorClient(getenv("ATLAS_CONNECTION_URL"))
        engine = AIOEngine(client=client, database=getenv("DATABASE_NAME"))
        yield engine
    finally:
        client.close()