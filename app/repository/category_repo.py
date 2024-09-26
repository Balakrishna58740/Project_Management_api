from fastapi import HTTPException
from app.dto.category_dto import CategoryDTO, CategoryDTOResponse
from app.models.category_model import Category
from bson import ObjectId
from app.config.db_config import mongodb

class CategoryRepo():
    @staticmethod
    async def get_categories():
        try:
            cursor = mongodb.collections['categories'].find({}).to_list(length=None)
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting categories: {e}")

    @staticmethod
    async def get_category_by_id(category_id: str):
        try:
            id = ObjectId(category_id)
            cursor = await mongodb.collections['categories'].find_one({"_id": id})
            if cursor is None:
                raise HTTPException(status_code=404, detail="Category not found")
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error finding category: {e}")

    @staticmethod
    async def create_category(category: Category):
        try:
            cursor = await mongodb.collections["categories"].insert_one(category.dict(exclude_unset=True))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Invalid data: {e}")
        return {"message": "Category created successfully"}

    @staticmethod
    async def update_category(category_id: str, category: Category):
        try:
            id = ObjectId(category_id)
            category_data = category.dict(exclude_unset=True)
            response = await mongodb.collections['categories'].update_one({"_id": id}, {"$set": category_data})
            if response.modified_count > 0:
                return {"message": "Category updated successfully"}
            else:
                raise HTTPException(status_code=404, detail="Category not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating category: {e}")

    @staticmethod
    async def delete_category(category_id: str):
        try:
            id = ObjectId(category_id)
            response = await mongodb.collections['categories'].delete_one({"_id": id})
            if response.deleted_count > 0:
                return {"message": "Category deleted successfully"}
            else:
                raise HTTPException(status_code=404, detail="Category not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting category: {e}")