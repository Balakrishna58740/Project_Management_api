from fastapi import HTTPException
from app.dto.project_dto import ProjectDTO, ProjectResponseDTO
from app.models.project_model import Project
from bson import ObjectId
from app.config.db_config import mongodb

class ProjectRepo():
    @staticmethod
    async def get_projects():
        try:
            cursor = mongodb.collections['projects'].find({}).to_list(length=None)
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting projects: {e}")

    @staticmethod
    async def get_project_by_id(project_id: str):
        try:
            id = ObjectId(project_id)
            cursor = await mongodb.collections['projects'].find_one({"_id": id})
            if cursor is None:
                raise HTTPException(status_code=404, detail="Project not found")
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error finding project: {e}")

    @staticmethod
    async def create_project(project: Project):
        try:
            cursor = await mongodb.collections["projects"].insert_one(project.dict(exclude_unset=True))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Invalid data: {e}")
        return {"message": "Project created successfully"}

    @staticmethod
    async def update_project(project_id: str, project: Project):
        try:
            id = ObjectId(project_id)
            project_data = project.dict(exclude_unset=True)
            response = await mongodb.collections['projects'].update_one({"_id": id}, {"$set": project_data})
            if response.modified_count > 0:
                return {"message": "Project updated successfully"}
            else:
                raise HTTPException(status_code=404, detail="Project not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating project: {e}")

    @staticmethod
    async def delete_project(project_id: str):
        try:
            id = ObjectId(project_id)
            response = await mongodb.collections['projects'].delete_one({"_id": id})
            if response.deleted_count > 0:
                return {"message": "Project deleted successfully"}
            else:
                raise HTTPException(status_code=404, detail="Project not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting project: {e}")