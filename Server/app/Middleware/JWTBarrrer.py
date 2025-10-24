from fastapi import Request, HTTPException
from jose import jwt
from app.Core.Config import settings
from app.Core.ConnectDB import collection_user

async def get_current_user (request: Request):
    try:
        token = None
        token = request.cookies.get("token")
        if not token:
            return HTTPException(status_code=404, detail="Token not found")
        payload = jwt.decode(token, settings.SERECT_KEY, algorithms=["HS256"])
        email = payload.get("sub")
        if email is None:
            return HTTPException(status_code=404, detail="Token not found")
        user = await collection_user.find_one({"email": email})
        if not user:
            return HTTPException(status_code=404, detail="User not found")
        
        return user
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    
