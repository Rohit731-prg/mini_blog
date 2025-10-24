from app.Database.Model.UserModel import UserModel, LoginModel
from fastapi import HTTPException
from app.Core.ConnectDB import collection_user
from app.Database.Schema.UserSchema import login_Schema
from app.Utils.password_hash import verify_hash

async def RegisterCurd(user: UserModel) -> dict:
    try:
        await collection_user.insert_one(user.dict())
        return {
            "message": "User registered successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def loginCurd(user: LoginModel) -> dict:
    try:
        exist = await collection_user.find_one({"email": user.email})
        if not exist:
            raise HTTPException(status_code=404, detail="User not found")
        
        match = verify_hash(user.password, exist["password"])
        if not match:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return {
            "message": "User logged in successfully",
            "user": login_Schema(exist)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))