from app.Core.ConnectDB import collection_user
from bson import ObjectId

async def Single_Post(port) -> dict:
    user = await collection_user.find_one({ "_id": ObjectId(port["user"]) })
    print(user)
    return {
        "title": str(port["title"]),
        "content": str(port["content"]),
        "image": str(port["image"]),
        "createAt": str(port["createAt"]),
        "user": {
            "name": str(user["name"]),
            "email": str(user["email"]),
            "image": str(user["image"]),
        } if user else None
    }

async def Post_list_Schema(posts) -> list:
    result = []
    for post in posts:
        result.append(await Single_Post(post))

    return result