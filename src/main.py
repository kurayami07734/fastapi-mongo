from contextlib import asynccontextmanager

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers.company import company_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield


app = FastAPI(title="Rest API with MongoDB using Motor", lifespan=lifespan)

app.include_router(company_router, prefix="/companies", tags=['Companies'])

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")