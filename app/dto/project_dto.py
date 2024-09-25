from bson import DBRef, ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional

class ProjectDTO(BaseModel):
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    user: Optional[List[DBRef]] = None  # Keep using DBRef directly

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types
        json_encoders = {
            ObjectId: str,  # Convert ObjectId to string for JSON serialization
            DBRef: lambda v: {
                "collection": v.collection,
                "id": str(v.id),  # Ensure ID is serialized as string
                "database": v.database,
            },
        }

class ProjectResponseDTO(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    user: Optional[List[DBRef]] = None  # Keep using DBRef directly

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types
        json_encoders = {
            ObjectId: str,  # Convert ObjectId to string for JSON serialization
            DBRef: lambda v: {
                "collection": v.collection,
                "id": str(v.id),  # Ensure ID is serialized as string
                "database": v.database,
            },
        }
