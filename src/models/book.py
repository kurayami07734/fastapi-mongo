from pydantic import BaseModel, Field


class Book(BaseModel):
    name: str
    release_date: str = Field(datetime_format="%Y-%m-%d")
    author: str
    rating: float = Field(gte=0.0, lte=10.0)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "A brief history of time",
                "release_date": "1998-04-01",
                "author": "Steven Hawking",
                "rating": 7.5,
            } 
        }