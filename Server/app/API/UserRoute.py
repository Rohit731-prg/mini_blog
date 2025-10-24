from fastapi import APIRouter, HTTPException, Form, UploadFile, Response
from app.Core.ConnectDB import collection_user
from app.Utils.cloudinary import upload_image
from app.Curd.UserCurd import RegisterCurd, loginCurd
from app.Database.Model.UserModel import UserModel, LoginModel
from app.Utils.JwtToken import generate_token
from app.Utils.password_hash import generate_hash

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/register")
async def RegisterRouter(
    response: Response,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    image: UploadFile = Form(...)
) -> dict:
    try:
        exist = await collection_user.find_one({"email": email})
        if exist:
            raise HTTPException(status_code=400, detail="User already exists")
        
        image_url = upload_image(image.file)
        hashPassword = generate_hash(password)
        newUser = {
            "name": name,
            "email": email,
            "password": hashPassword,
            "image": image_url["url"],
            "image_id": image_url["public_id"]
        }
        newUser = UserModel(**newUser)
        response.status_code = 201
        return await RegisterCurd(newUser)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/login")
async def LoginRoute(resqest: LoginModel, response: Response) -> dict:
    print("Login Route hit:", resqest)
    try:
        token = generate_token(dict(resqest))
        response.set_cookie(key="token", value=token, httponly=True)
        response.status_code = 200
        return await loginCurd(resqest)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))