from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.config.logger_config import get_logger
from app.models.todos_model import Todos
from app.dto.todos_dto import TodosDTO, TodosResponseDTO
from app.utils.response_utils import get_response
from app.service.todos_service import TodosService

todos_route = APIRouter()
logger = get_logger()

@todos_route.get("/todos")
async def get_todos():
    logger.info("/ENDPOINT CALLED: /TODOS (GET) \n DATA RECEIVED")
    response = await TodosService.get_todos()
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Todos Retrieved Successfully", data=response, status_code=200)

@todos_route.get("/todos/{todos_id}")
async def get_todos_by_id(todos_id: str):
    logger.info(f"ENDPOINT CALLED: /TODOS/{todos_id} (GET)")
    response = await TodosService.get_todos_by_id(todos_id)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Todos Retrieved Successfully", data=response, status_code=200)

@todos_route.post("/todos")
async def create_todos(todos: TodosDTO):
    logger.info(f"ENDPOINT CALLED: /TODOS (POST) \n DATA SENT : {todos.dict()}")
    response = await TodosService.create_todos(todos)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Todos Created Successfully", data=response, status_code=201)

@todos_route.put("/todos/{todos_id}")
async def update_todos(todos_id: str, todos: TodosDTO):
    logger.info(f"ENDPOINT CALLED: /TODOS/{todos_id} (PUT) \n DATA SENT : {todos.dict()}")
    response = await TodosService.update_todos(todos_id, todos)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Todos Updated Successfully", data=response, status_code=200)

@todos_route.delete("/todos/{todos_id}")
async def delete_todos(todos_id: str):
    logger.info(f"ENDPOINT CALLED: /TODOS/{todos_id} (DELETE)")
    try:
        response = await TodosService.delete_todos(todos_id)
        logger.info(f"RESPONSE: {response}")
        return get_response(status="success", message="Todos Deleted Successfully", status_code=200)
    except HTTPException as e:
        logger.error(f"ERROR OCCURRED")
        raise e