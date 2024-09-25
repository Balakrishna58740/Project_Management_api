from typing import List, Optional
from bson import DBRef, ObjectId
from pydantic import BaseModel, validator


class User(BaseModel):
    email: str
    password: str
    role: str
    project: Optional[List[DBRef]] = None

    @validator('role')
    def role_is_valid(cls, v):
        if v not in ['admin', 'user']:
            raise ValueError("Role must be either 'admin' or 'user'")
        return v

    @validator('project', pre=True)
    def convert_to_dbref(cls, v):
        if isinstance(v, list):
            return [DBRef('projects', ObjectId(item)) if isinstance(item, str) else item for item in v]
        return v

    @validator('user_id', pre=True, always=True)
    def validate_user_id(cls, v):
        if isinstance(v, str):
            try:
                # Convert user_id string to a DBRef
                return DBRef(collection="users", id=ObjectId(v))
            except Exception:
                raise ValueError("Invalid user_id format. Must be a valid ObjectId string.")
        return v

    class Config:
        arbitrary_types_allowed = True
