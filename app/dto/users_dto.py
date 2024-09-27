from typing import List, Optional
from bson import DBRef, ObjectId
from pydantic import BaseModel, ConfigDict, Field, validator

class UserDTO(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    role: str
    project: Optional[List[DBRef]] = None

    @validator('role')
    def role_is_valid(cls, v):
        if v not in ['admin', 'user']:
            raise ValueError("Role must be either 'admin' or 'user'")
        return v
    
    class Config:
        arbitrary_types_allowed = True

class UserDTOResponse(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    email: Optional[str] = None
    role: str
    project: Optional[List[str]] = None  # Keep as List[str] for output

    @validator('project', pre=True)
    def convert_str_to_dbref(cls, v):
        if isinstance(v, list):
            return [DBRef('projects', ObjectId(item)) if isinstance(item, str) else item for item in v]
        return v

    @validator('id', pre=True)
    def convert_objectid_to_str(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v

    class Config:
        populate_by_name = True
        json_encoders = {
            ObjectId: str,
            DBRef: lambda ref: str(ref.id)
        }
        arbitrary_types_allowed = True
