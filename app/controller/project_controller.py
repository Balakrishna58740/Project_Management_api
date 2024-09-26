from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.config.logger_config import get_logger
from app.models.project_model import Project
from app.dto.project_dto import ProjectDTO, ProjectDTOResponse
from app.utils.response_utils import get_response
from app.service.project_service import ProjectService

project_route = APIRouter()
logger = get_logger()

@project_route.get("/project")
async def get_projects():
    logger.info("/ENDPOINT CALLED: /PROJECT (GET) \n DATA RECEIVED")
    response = await ProjectService.get_projects()
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Projects Retrieved Successfully", data=response, status_code=200)

@project_route.get("/project/{project_id}")
async def get_project_by_id(project_id: str):
    logger.info(f"ENDPOINT CALLED: /PROJECT/{project_id} (GET)")
    response = await ProjectService.get_project_by_id(project_id)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Project Retrieved Successfully", data=response, status_code=200)

@project_route.post("/project")
async def create_project(project: ProjectDTO):
    logger.info(f"ENDPOINT CALLED: /PROJECT (POST) \n DATA SENT : {project.dict()}")
    response = await ProjectService.create_project(project)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Project Created Successfully", data=response, status_code=201)

@project_route.put("/project/{project_id}")
async def update_project(project_id: str, project: ProjectDTO):
    logger.info(f"ENDPOINT CALLED: /PROJECT/{project_id} (PUT) \n DATA SENT : {project.dict()}")
    response = await ProjectService.update_project(project_id, project)
    logger.info(f"RESPONSE: {response}")
    return get_response(status="success", message="Project Updated Successfully", data=response, status_code=200)

@project_route.delete("/project/{project_id}")
async def delete_project(project_id: str):
    logger.info(f"ENDPOINT CALLED: /PROJECT/{project_id} (DELETE)")
    try:
        response = await ProjectService.delete_project(project_id)
        logger.info(f"RESPONSE: {response}")
        return get_response(status="success", message="Project Deleted Successfully", status_code=200)
    except HTTPException as e:
        logger.error(f"ERROR OCCURRED")
        raise e