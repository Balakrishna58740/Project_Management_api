from bson import ObjectId, DBRef
from pydantic import BaseModel, field_validator
from typing import Optional

class Todos(BaseModel):
    todos_name: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    todos_description: Optional[str]
    priority: Optional[str]
    status: Optional[str]
    category_id: Optional[DBRef]
    user_id: Optional[DBRef]

    @field_validator('category_id', 'user_id', mode='before')
    def convert_to_dbref(cls, v, info):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId for {info.field_name}")
        return DBRef(collection=info.field_name[:-3], id=ObjectId(v))

    class Config:
        arbitrary_types_allowed = True
