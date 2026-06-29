import time
from PIL import Image, ImageFilter
from .models import Photo

def process_image_task(photo_id):
    photo = Photo.objects.get(pk=photo_id)
    # Simulate a "heavy" task
    time.sleep(10) 
    
    img = Image.open(photo.image.path)
    img = img.filter(ImageFilter.GaussianBlur(radius=15))
    img.save(photo.image.path)
    
    photo.processed = True
    photo.save()