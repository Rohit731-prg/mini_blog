from fastapi import APIRouter, Response, Form, UploadFile, HTTPException, Depends
from app.Utils.cloudinary import upload_image
from app.Curd.PostCurd import createPostCurd, getAllPostCurd
from app.Database.Model.PostModel import PostModel
from app.Middleware.JWTBarrrer import get_current_user

router = APIRouter(prefix="/post", tags=["Post"])

@router.post("/createPost")
async def createPostRoute(
    response: Response,
    current_user: dict = Depends(get_current_user),
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = Form(...),
    user: str = Form(...)
) -> dict:
    try:
        image_url = upload_image(image.file)
        newPost = {
            "title": title,
            "content": content,
            "image": image_url["url"],
            "image_id": image_url["public_id"],
            "user": user
        }
        res = await createPostCurd(PostModel(**newPost))
        response.status_code = 201
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/getAllPosts")
async def getAllPostsRoute(current_user: dict = Depends(get_current_user)) -> list[dict]:
    try:
        res = await getAllPostCurd()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))