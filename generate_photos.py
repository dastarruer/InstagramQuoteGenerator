from api import API_KEY

from random import choice
from requests import get

class ImageGenerator:
    def request_pexels_api(self, num_of_photos: int):
        """
        Requests a random photo from the Pexels API.
        """

        # This header is used to send our API key to the API for verification
        headers = {
            "Authorization": API_KEY
        }

        # The parameters that will be sent to the API
        categories = ["abstract", "landscape", "ocean", "sky"]

        # The category that the API will search for
        chosen_category = choice(categories)

        # The parameters that will be sent to the API
        params = {
            "query": chosen_category,
            "orientation": "landscape",
            "per_page": num_of_photos
        }

        print(f"Searching for '{params["query"]}'...")

        # Get the JSON response from the API
        response = get("https://api.pexels.com/v1/search", headers=headers, params=params).json()
        print(f"Width: {response["photos"][0]["width"]} Height: {response["photos"][0]["height"]}")
        return response
    

    def get_pexels_image(self, num_of_photos: int):
        """
        Save a Pexels image using its URL. This URL is fetched from request_pexels_api().
        """
        # Get a photo from the Pexels API
        photo = self.request_pexels_api(num_of_photos)

        # Get the URL of the photo
        photo_url = photo["photos"][0]["src"]["original"]

        # Get the content of the URL
        photo = get(photo_url)

        # Save the image
        filename = "image.JPEG"
        with open(filename, 'wb') as f:
            f.write(photo.content)
        print("Done!")

image_generator = PhotoGenerator()
