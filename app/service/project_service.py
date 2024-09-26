from typing import List
from app.config.logger_config import get_logger
from app.models.project_model import Project
from app.dto.project_dto import ProjectDTO, ProjectDTOResponse
from fastapi import HTTPException
from app.repository.project_repo import ProjectRepo

class ProjectService():
    @staticmethod
    async def get_projects():
        result = await ProjectRepo.get_projects()
        project_list = [ProjectDTOResponse(**project) for project in result]
        return project_list
    
    @staticmethod
    async def create_project(projectdto: ProjectDTO):
        project = Project(**projectdto.dict(exclude_unset=True))
        result = await ProjectRepo.create_project(project)
        if result:
            return {"message": "Project created successfully"}
        raise HTTPException(status_code=500, detail="Failed to create project")
    
    @staticmethod
    async def update_project(project_id: str, projectdto: ProjectDTO):
        project = Project(**projectdto.dict(exclude_unset=True))
        result = await ProjectRepo.update_project(project_id, project)
        if result:
            return {"message": "Project updated successfully"}
        raise HTTPException(status_code=500, detail="Failed to update project")
    
    @staticmethod
    async def delete_project(project_id: str):
        result = await ProjectRepo.delete_project(project_id)
        if result:
            return {"message": "Project deleted successfully"}
        raise HTTPException(status_code=500, detail="Failed to delete project")
    
    @staticmethod
    async def get_project_by_id(project_id: str):
        try:
            result = await ProjectRepo.get_project_by_id(project_id)
            result["_id"] = str(result["_id"])  # Convert ObjectId to string
            return ProjectDTOResponse(**result)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")