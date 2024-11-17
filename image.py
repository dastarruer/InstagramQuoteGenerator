from requests import get
from api import API_KEY

headers = {
    "Authorization": API_KEY
}

api_query = "https://api.pexels.com/v1/search?query=abstract&orientation=landscape&per_page=1"

photo = get(api_query, headers=headers).json() 

photo_url = photo["photos"][0]["src"]["original"]
photo = get(photo_url)

with open("image.JPEG", 'wb') as f:
    f.write(photo.content)
