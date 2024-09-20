from contextlib import asynccontextmanager

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from motor.motor_asyncio import AsyncIOMotorClient

from src.routers.book import book_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()

    yield


app = FastAPI(title="Rest API with MongoDB using Motor", lifespan=lifespan)

app.include_router(book_router, prefix="/books", tags=['Books'])

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")