from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.config.logger_config import get_logger
from app.models.category_model import Category
from app.dto.category_dto import CategoryDTO, CategoryDTOResponse
from app.utils.response_utils import get_response
from app.service.category_service import CategoryService

category_route = APIRouter()
logger = get_logger()

@category_route.get("/category")
async def get_categories():
    logger.info("/ENDPOINT CALLED: /CATEGORY (GET) \n DATA RECEIVED")
    response = await CategoryService.get_categories()
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Categories Retrieved Successfully", data=response, status_code=200)

@category_route.get("/category/{category_id}")
async def get_category_by_id(category_id: str):
    logger.info(f"ENDPOINT CALLED: /CATEGORY/{category_id} (GET)")
    response = await CategoryService.get_category_by_id(category_id)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Category Retrieved Successfully", data=response, status_code=200)

@category_route.post("/category")
async def create_category(category: CategoryDTO):
    logger.info(f"ENDPOINT CALLED: /CATEGORY (POST) \n DATA SENT : {category.dict()}")
    response = await CategoryService.create_category(category)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Category Created Successfully", data=response, status_code=201)

@category_route.put("/category/{category_id}")
async def update_category(category_id: str, category: CategoryDTO):
    logger.info(f"ENDPOINT CALLED: /CATEGORY/{category_id} (PUT) \n DATA SENT : {category.dict()}")
    response = await CategoryService.update_category(category_id, category)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Category Updated Successfully", data=response, status_code=200)

@category_route.delete("/category/{category_id}")
async def delete_category(category_id: str):
    logger.info(f"ENDPOINT CALLED: /CATEGORY/{category_id} (DELETE)")
    try:
        response = await CategoryService.delete_category(category_id)
        logger.info(f"RESPONSE: {response}")
        return get_response(status="success", message="Category Deleted Successfully", status_code=200)
    except HTTPException as e:
        logger.error(f"ERROR OCCURRED")
        raise e