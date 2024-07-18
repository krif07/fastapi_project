from pydantic import BaseModel
from datetime import datetime
from typing import List


class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    category: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

