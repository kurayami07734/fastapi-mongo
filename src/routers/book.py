from fastapi.exceptions import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from fastapi import APIRouter, Depends

from src.models.book import Book
from src.dependencies import get_mongo_client

book_router = APIRouter()

@book_router.get("/", response_model=list[Book])
async def book_list(client: AsyncIOMotorDatabase = Depends(get_mongo_client)):
    try:
        book_collection = client.get_collection("books")
        book_list = [b async for b in book_collection.find()]
        return book_list
    except:
        return HTTPException(status_code=404)
