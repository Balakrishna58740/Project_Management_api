from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, logger
from app.config.logger_config import get_logger
from app.models.user_model import User
from app.dto.users_dto import UserDTO,UserDTOResponse
from app.utils.response_utils import get_response
from app.service.users_service import UserService

user_route = APIRouter()
logger = get_logger()

@user_route.get("/user")
async def get_user():
    logger.info("/ENDPOINT CALLED: /USER (GET) \n DATA RECEIVED")
    response = await UserService.get_user()
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Academic Calendar Retrieved Successfully", data=response, status_code=200)

@user_route.get("/user/{user_id}")
async def get_user_by_id(user_id: str):
    logger.info(f"ENDPOINT CALLED: /USER/{user_id} (GET)")
    response = await UserService.get_user_by_id(user_id)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="User Retrieved Successfully", data=response, status_code=200)

@user_route.post("/user")
async def create_user(user : UserDTO):
    logger.info(f"ENDPOINT CALLED: /USER (POST) \n DATA SENT : {user.dict()}")
    response = await UserService.create_user(user)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="User Created Successfully", data=response, status_code=201)

@user_route.put("/user/{user_id}")
async def update_user(user_id: str, user : UserDTO):
    logger.info(f"ENDPOINT CALLED: /USER/{user_id} (PUT) \n DATA SENT : {user.dict()}")
    response = await UserService.update_user(user_id, user)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="User Updated Successfully", data=response, status_code=200)

@user_route.delete("/user/{user_id}")
async def delete_user(user_id: str):
    logger.info(f"ENDPOINT CALLED: /USER/{user_id} (DELETE)")
    try:
        response = await UserService.delete_user(user_id)
        logger.info(f"RESPONSE: {response}")
        return get_response(status="success", message="User Deleted Successfully", status_code=200)
    except HTTPException as e:
        logger.error(f"ERROR OCCURRED")
        raise e
