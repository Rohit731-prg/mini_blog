from app.Core.Config import settings
from datetime import datetime, timedelta
from jose import jwt

secret_key = settings.SERECT_KEY
algorithm = "HS256"
expair_minutes = 300

def generate_token(data: dict) -> str:
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=expair_minutes)
    print("Expair Time : ", expire_time)
    to_encode.update({"exp": expire_time})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt