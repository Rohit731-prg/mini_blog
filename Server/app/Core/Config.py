from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = ""
    CLOUDINARY_NAME: str = ""
    CLOUDINARY_KEY: str = ""
    CLOUDINARY_SECRET: str = ""
    SERECT_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()