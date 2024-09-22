from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body

from fastapi import APIRouter, Depends
from odmantic import AIOEngine, ObjectId
from pydantic import ValidationError

from src.models.company import Company, PatchCompany

from src.dependencies import db_engine

company_router = APIRouter()


@company_router.get("/", response_model=list[Company])
async def company_list(engine: AIOEngine = Depends(db_engine)):
    companies = []
    async for c in engine.find(Company):
        companies.append(c)
    return companies


@company_router.post("/", response_model=Company)
async def create_company(
    company: Company = Body(...), engine: AIOEngine = Depends(db_engine)
):
    await engine.save(company)
    return company


@company_router.get("/{id}", response_model=Company)
async def retrieve_company(id: ObjectId, engine: AIOEngine = Depends(db_engine)):
    company = await engine.find_one(Company, Company.id == id)
    if company is None:
        raise HTTPException(404)
    return company


@company_router.patch("/{id}", response_model=PatchCompany)
async def update_company(
    id: ObjectId,
    patch: PatchCompany = Body(...),
    engine: AIOEngine = Depends(db_engine),
):
    company = await engine.find_one(Company, Company.id == id)
    if company is None:
        raise HTTPException(404)
    try:
        company.model_update(patch)
    except ValidationError:
        raise HTTPException(400, detail="Validation Error")
    await engine.save(company)
    return company


@company_router.delete("/{id}", response_model=Company)
async def delete_company(id: ObjectId, engine: AIOEngine = Depends(db_engine)):
    company = await engine.find_one(Company, Company.id == id)
    if company is None:
        raise HTTPException(404)
    await engine.delete(company)
    return company