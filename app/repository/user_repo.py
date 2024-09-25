from urllib import response
from fastapi import HTTPException
from app.dto.users_dto import UserDTOResponse,UserDTO
from app.models.user_model import User
from bson import ObjectId
from app.config.db_config import mongodb
class UserRepo():
    @staticmethod
    async def get_user():
        try:
            cursor = mongodb.collections['users'].find({}).to_list(length=None)
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting user: {e}")
    @staticmethod  
    async def get_user_by_id(user_id: str):
        try:
            id = ObjectId(user_id)
            cursor =  await mongodb.collections['users'].find_one({"_id": id})
            if cursor is None:
                raise HTTPException(status_code=404, detail="User not found")
            return cursor
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error to find user: {e}")    
    @staticmethod  
    async def create_user(user :User):
        try:
            cursor = await mongodb.collections["users"].insert_one(user.dict(exclude_unset=True))
        except:
            raise HTTPException(status_code=500, detail="Invalid data ")
        return {"message":"user created successfully"}
    
    @staticmethod  
    async def update_user(user_id :str,user:User):
        try: 
            id = ObjectId(user_id)
            user_data = user.dict(exclude_unset=True)
            response = await mongodb.collections['users'].update_one({"_id":id},{"$set":user_data})
            if response:
                return {"User updated successfully"}
            else:
                raise HTTPException(status_code=404,detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500,detail=f"Error to update user : {e}")
    
    @staticmethod      
    async def delete_user(user_id: str):
        try:
            user = ObjectId(user_id)
            response = await mongodb.collections['users'].delete_one({"_id": user})
            if response.deleted_count > 0:
                return {"message": "User deleted successfully"}
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error to delete user: {e}")

            