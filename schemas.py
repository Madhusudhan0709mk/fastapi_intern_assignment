# schemas.py
from pydantic import BaseModel

class PropertyBase(BaseModel):
    name: str
    owner_name: str

class PropertyCreate(PropertyBase):
    locality_id: int

class PropertyUpdate(PropertyBase):
    locality_id: int

class Property(PropertyBase):
    id: int
    locality_id: int

    class Config:
        orm_mode = True

class LocalityBase(BaseModel):
    name: str

class Locality(LocalityBase):
    id: int
    properties: list[Property] = []

    class Config:
        orm_mode = True
