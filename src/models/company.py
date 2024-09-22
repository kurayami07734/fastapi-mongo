from typing import Optional

from odmantic import Field, Model
from pydantic import BaseModel


class Company(Model):
    name: str
    sector: Optional[str]
    stock_price: float = Field(ge=0.0)
    market_cap: str

    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "name": "Twiyo",
    #             "sector": "Capital Goods",
    #             "stock_price": 34.84,
    #             "market_cap": "$229.33M",
    #         }
    #     }

class PatchCompany(BaseModel):
    name: Optional[str] = None
    sector: Optional[str] = None
    stock_price: Optional[float] = None
    market_cap: Optional[str] = None