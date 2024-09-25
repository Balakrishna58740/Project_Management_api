from typing import List, Optional
from bson import DBRef, ObjectId
from pydantic import BaseModel, validator

class category(BaseModel):
    category_name : Optional[str] = None