def login_Schema(user: dict) -> dict:
    return {
        "_id": str(user["_id"]),
        "name": str(user["name"]),
        "email": str(user["email"]),
        "image": str(user["image"])
    }