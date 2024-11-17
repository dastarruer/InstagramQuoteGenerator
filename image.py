from api import API_KEY

from random import choice
from requests import get

# This header is used to send our API key to the API for verification
headers = {
    "Authorization": API_KEY
}

# The parameters that will be sent to the API
categories = ["abstract", "landscape", "ocean", "sky"]
num_of_photos = "1"
orientation = "landscape"

# The category that the API will search for
chosen_category = choice(categories)

print(f"Searching for '{chosen_category}'...")

api_query = f"https://api.pexels.com/v1/search?query={chosen_category}&orientation={orientation}&per_page={num_of_photos}"

photo = get(api_query, headers=headers).json() 

photo_url = photo["photos"][0]["src"]["original"]
photo = get(photo_url)

with open("image.JPEG", 'wb') as f:
    f.write(photo.content)

print("Done!")