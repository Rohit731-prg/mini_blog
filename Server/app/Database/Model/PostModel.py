from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostModel(BaseModel):
    title: str
    content: str
    image: Optional[str] = None
    imge_id: Optional[str] = None
    user: str
    createAt: float = datetime.timestamp(datetime.now())
