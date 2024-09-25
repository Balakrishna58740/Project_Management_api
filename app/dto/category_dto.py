from typing import List, Optional
from bson import DBRef, ObjectId
from pydantic import BaseModel, Field, validator

class Categorydto(BaseModel):
    category_name : Optional[str] = None

class CategoryResponseDto(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    category_name : Optional[str] = None