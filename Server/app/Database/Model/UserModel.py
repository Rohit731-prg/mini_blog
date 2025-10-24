from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    name: str
    email: str
    password: str
    image: Optional[str] = None
    image_id: Optional[str] = None

class LoginModel(BaseModel):
    email: str
    password: str