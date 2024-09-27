from typing import List, Optional
from bson import DBRef, ObjectId
from pydantic import BaseModel, validator

class Project(BaseModel):
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    user: Optional[List[DBRef]] = None  # Ensure user is a list of DBRef

    @validator('user', pre=True)
    def convert_to_dbref(cls, v):
        if isinstance(v, list):
            return [DBRef('users', ObjectId(item)) if isinstance(item, str) else item for item in v]
        return v

    class Config:
        arbitrary_types_allowed = True  # Allow DBRef
        # json_encoders = {
        #     ObjectId: str,  # Convert ObjectId to string
        #     DBRef: lambda dbref: {
        #         "collection": dbref.collection,  # Include collection name
        #         "id": str(dbref.id),  # Serialize DBRef ID as string
        #         "database": dbref.database,  # Include database name
        #     }
        # }
