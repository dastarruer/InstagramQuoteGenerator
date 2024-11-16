from requests import get
from api import API_KEY

headers = {
    "Authorization": API_KEY
}

print(get("https://api.pexels.com/v1/curated?page=2&per_page=1", headers=headers).json())