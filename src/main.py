from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers.book import book_router

app = FastAPI(title="Rest API with MongoDB using Motor")

app.include_router(book_router, prefix="/books", tags=['Books'])

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")