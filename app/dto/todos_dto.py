# from bson.dbref import DBRef
# from pydantic import BaseModel, validator
# from typing import Optional

# class TodosDTO(BaseModel):
#     todos_name: Optional[str] = None
#     start_date:Optional[str] = None
#     end_date: Optional[str] = None
#     todos_description: Optional[str] = None
#     priority: Optional[str] = None
#     status: Optional[str] = None
#     project_id: Optional[str] = None
#     user_id: Optional[str] = None

#     class Config:
#         arbitrary_types_allowed = True

# class TodosDTOResponse(BaseModel):
#     todos_id: Optional[str] = None
#     todos_name: Optional[str] = None
#     start_date: Optional[str] = None
#     end_date: Optional[str] = None
#     todos_description: Optional[str] = None
#     priority: Optional[str] = None
#     status: Optional[str] = None
#     project_id: Optional[str] = None
#     user_id: Optional[str] = None

#     @validator('project_id', 'user_id')
#     def convert_dbref_to_str(cls, v):
#         if isinstance(v, DBRef):
#             return str(v)
#         return v
    
#     class Config:
#         arbitrary_types_allowed = True
#         json_encoders = {
#             DBRef: lambda dbref: {
#                 'collection': dbref.collection,
#                 'id': str(dbref.id)
#             }}


from bson.dbref import DBRef
from pydantic import BaseModel, field_validator
from typing import Optional

class TodosDTO(BaseModel):
    todos_name: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    todos_description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    project_id: Optional[str] = None
    user_id: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class TodosResponseDTO(BaseModel):
    todos_id: Optional[str] = None
    todos_name: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    todos_description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    project_id: Optional[str] = None
    user_id: Optional[str] = None

    @field_validator('project_id', 'user_id')
    def convert_dbref_to_str(cls, v, info):
        if isinstance(v, DBRef):
            return str(v)
        return v
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            DBRef: lambda dbref: {
                'collection': dbref.collection,
                'id': str(dbref.id)
            }
        }
