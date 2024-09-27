from typing import List
from app.config.logger_config import get_logger
from app.models.todos_model import Todos
from app.dto.todos_dto import TodosDTO,TodosResponseDTO
from fastapi import HTTPException
from app.repository.todos_repo import todosRepo

class TodosService():
    @staticmethod
    async def get_todos():
        result = await todosRepo.get_todoss()
        todos_list = [TodosResponseDTO(**todos) for todos in result]
        return todos_list
    
    @staticmethod
    async def create_todos(todosdto: TodosDTO):
        todos = todos(**todosdto.dict(exclude_unset=True))
        result = await todosRepo.create_todos(todos)
        if result:
            return {"message": "todos created successfully"}
        raise HTTPException(status_code=500, detail="Failed to create todos")
    
    @staticmethod
    async def update_todos(todos_id: str, todosdto: TodosDTO):
        todos = todos(**todosdto.dict(exclude_unset=True))
        result = await todosRepo.update_todos(todos_id, todos)
        if result:
            return {"message": "todos updated successfully"}
        raise HTTPException(status_code=500, detail="Failed to update todos")
    
    @staticmethod
    async def delete_todos(todos_id: str):
        result = await todosRepo.delete_todos(todos_id)
        if result:
            return {"message": "todos deleted successfully"}
        raise HTTPException(status_code=500, detail="Failed to delete todos")
    
    @staticmethod
    async def get_todos_by_id(todos_id: str):
        try:
            result = await todosRepo.get_todos_by_id(todos_id)
            result["_id"] = str(result["_id"])  # Convert ObjectId to string
            return TodosResponseDTO(**result)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")