from typing import List
from app.config.logger_config import get_logger
from app.models.category_model import Category
from app.dto.category_dto import CategoryDTO, CategoryDTOResponse
from fastapi import HTTPException
from app.repository.category_repo import CategoryRepo

class CategoryService():
    @staticmethod
    async def get_categories():
        result = await CategoryRepo.get_categories()
        category_list = [CategoryDTOResponse(**category) for category in result]
        return category_list
    
    @staticmethod
    async def create_category(categorydto: CategoryDTO):
        category = Category(**categorydto.dict(exclude_unset=True))
        result = await CategoryRepo.create_category(category)
        if result:
            return {"message": "Category created successfully"}
        raise HTTPException(status_code=500, detail="Failed to create category")
    
    @staticmethod
    async def update_category(category_id: str, categorydto: CategoryDTO):
        category = Category(**categorydto.dict(exclude_unset=True))
        result = await CategoryRepo.update_category(category_id, category)
        if result:
            return {"message": "Category updated successfully"}
        raise HTTPException(status_code=500, detail="Failed to update category")
    
    @staticmethod
    async def delete_category(category_id: str):
        result = await CategoryRepo.delete_category(category_id)
        if result:
            return {"message": "Category deleted successfully"}
        raise HTTPException(status_code=500, detail="Failed to delete category")
    
    @staticmethod
    async def get_category_by_id(category_id: str):
        try:
            result = await CategoryRepo.get_category_by_id(category_id)
            result["_id"] = str(result["_id"])  # Convert ObjectId to string
            return CategoryDTOResponse(**result)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")