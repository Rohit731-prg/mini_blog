from fastapi import FastAPI
from app.API.UserRoute import router as user_router
from app.API.PostRoute import router as post_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL like ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],  # Or specify: ["GET", "POST", "OPTIONS"]
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(post_router)