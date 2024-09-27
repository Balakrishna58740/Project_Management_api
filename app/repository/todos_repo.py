from fastapi import HTTPException
from app.models.todos_model import Todos
from bson import ObjectId
from app.config.db_config import mongodb

class todosRepo():
    @staticmethod
    async def get_todos():
        try:
            cursor = mongodb.collections['todos'].find({}).to_list(length=None)
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting todoss: {e}")

    @staticmethod  
    async def get_todos_by_id(todos_id: str):
        try:
            id = ObjectId(todos_id)
            cursor = await mongodb.collections['todos'].find_one({"_id": id})
            if cursor is None:
                raise HTTPException(status_code=404, detail="todos not found")
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error to find todos: {e}")

    @staticmethod  
    async def create_todos(todos: Todos):
        try:
            cursor = await mongodb.collections["todos"].insert_one(todos.dict(exclude_unset=True))
        except:
            raise HTTPException(status_code=500, detail="Invalid data")
        return {"message": "todos created successfully"}

    @staticmethod  
    async def update_todos(todos_id: str, todos: Todos):
        try: 
            id = ObjectId(todos_id)
            todos_data = todos.dict(exclude_unset=True)
            response = await mongodb.collections['todos'].update_one({"_id": id}, {"$set": todos_data})
            if response:
                return {"message": "todos updated successfully"}
            else:
                raise HTTPException(status_code=404, detail="todos not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error to update todos: {e}")

    @staticmethod      
    async def delete_todos(todos_id: str):
        try:
            todos = ObjectId(todos_id)
            response = await mongodb.collections['todos'].delete_one({"_id": todos})
            if response.deleted_count > 0:
                return {"message": "todos deleted successfully"}
            else:
                raise HTTPException(status_code=404, detail="todos not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error to delete todos: {e}")