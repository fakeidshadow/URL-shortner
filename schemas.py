from pydantic import BaseModel
from datetime import datetime

class LinkCreate(BaseModel):
    address: str

class LinkResponse(BaseModel):
    address: str
    code: str
    date: datetime

    class Config:
        from_attributes = True