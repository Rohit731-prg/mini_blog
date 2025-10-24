import cloudinary
import cloudinary.uploader
from app.Core.Config import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_NAME,
    api_key=settings.CLOUDINARY_KEY,
    api_secret=settings.CLOUDINARY_SECRET
)

def upload_image(image) -> dict:
    result = cloudinary.uploader.upload(image)
    return {
        "url": result["secure_url"],
        "public_id": result["public_id"]
    }