from api import API_NINJAS_KEY

from requests import get, codes


category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
headers = {
    'X-Api-Key':API_NINJAS_KEY
}

r = get(api_url, headers=headers)
if r.status_code == codes.ok:
    print(r.json())
else:
    print(r.status_code)