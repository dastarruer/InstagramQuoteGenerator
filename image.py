from PIL import Image
from requests import get
from api import API_KEY

headers = {
    "Authorization": API_KEY
}

photo = get("https://api.pexels.com/v1/curated?page=1&per_page=1", headers=headers).json() 
photo_url = photo["photos"][0]["src"]["original"]
photo = get(photo_url)

with open("image.JPEG", 'wb') as f:
    f.write(photo.content)
