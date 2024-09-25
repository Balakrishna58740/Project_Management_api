from typing import List, Optional
from bson import DBRef, ObjectId
from pydantic import BaseModel, validator

class User(BaseModel):
    email: str
    password: str
    role: str
    project: Optional[List[DBRef]] = None  # Ensure project is a list of DBRef

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

    class Config:
        arbitrary_types_allowed = True  # Allow DBRef type
        json_encoders = {
            ObjectId: str,  # Convert ObjectId to string
            DBRef: lambda dbref: {
                "collection": dbref.collection,  # Include collection name
                "id": str(dbref.id),  # Serialize DBRef ID as string
                "database": dbref.database,  # Include database name
            }
        }
