from app.Database.Model.PostModel import PostModel
from app.Core.ConnectDB import collection_post
from fastapi import HTTPException
from app.Database.Schema.PostSchema import Post_list_Schema

async def createPostCurd(post: PostModel) -> dict:
    try:
        await collection_post.insert_one(dict(post))
        return {"message": "Post created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def getAllPostCurd() -> list[dict]:
    try:
        posts = await collection_post.find().to_list(length=None)
        return await Post_list_Schema(posts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
