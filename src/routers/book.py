from fastapi import APIRouter

from src.models.book import Book

book_router = APIRouter()

@book_router.get("/", response_model=list[Book])
async def book_list():
    book = Book(**{
                "name": "A brief history of time",
                "release_date": "1998-04-01",
                "author": "Steven Hawking",
                "rating": 7.5,
            } )
    return [book] * 3