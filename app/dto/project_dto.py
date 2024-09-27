from bson import DBRef, ObjectId
from pydantic import BaseModel, Field, validator
from typing import Any, List, Optional

class ProjectDTO(BaseModel):
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    user: Optional[List[str]] = None 
     
class ProjectResponseDTO(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    user: Optional[List[DBRef]] = None  # Keep using DBRef directly

    @validator('user', pre=False, always=True)
    def convert_dbrefs_to_user_ids(cls, dbrefs: Optional[List[DBRef]]):
        if dbrefs is None:
            return None  # Return None if the input is None
        # Convert each DBRef back to its ID as a string
        return [str(dbref.id) for dbref in dbrefs if isinstance(dbref, DBRef)]
    
    @validator('id', pre=True, always=True)
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

