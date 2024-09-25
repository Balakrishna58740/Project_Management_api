from typing import List
from app.config.logger_config import get_logger
from app.models.user_model import User
from app.dto.users_dto import UserDTO,UserDTOResponse
from fastapi import HTTPException
from app.repository.user_repo import UserRepo
# from app.utils.password_utils import get_password_hash

class UserService():
    @staticmethod
    async def get_user():
        result = await UserRepo.get_user()
        user_list = [UserDTOResponse(**user) for user in result]
        return user_list
    
    @staticmethod
    async def create_user(userdto : UserDTO):
        # userdto.password = get_password_hash(userdto.password)
        user = User(**userdto.dict(exclude_unset=True))
        result = await UserRepo.create_user(user)
        if result:
            return {"message":"user created successfully"}
        raise HTTPException(status_code=500,detail="Failed to create user")
    
    @staticmethod
    async def update_user(user_id : str,userdto : UserDTO):
        user = User(**userdto.dict(exclude_unset=True))
        result = await UserRepo.update_user(user_id,user)
        if result:
            return {"message":"user updated successfully"}
        raise HTTPException(status_code=500,detail="Failed to update user")
    
    @staticmethod
    async def delete_user(user_id:str):
        result = await UserRepo.delete_user(user_id)
        if result:
            return {"message":"user deleted successfully"}
        raise HTTPException(status_code=500,detail="Failed to delete user")
    
    @staticmethod
    async def get_user_by_id(user_id: str):
        try:
            result = await UserRepo.get_user_by_id(user_id)
            result["_id"] = str(result["_id"])  # Convert ObjectId to string
            return UserDTOResponse(**result)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")