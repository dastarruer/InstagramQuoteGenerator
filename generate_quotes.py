from api import API_NINJAS_KEY

from requests import get, codes


category = 'happiness'
api_url = f'https://api.api-ninjas.com/v1/quotes?category={API_NINJAS_KEY}'
headers = {
    'X-Api-Key':API_NINJAS_KEY
}

r = get(api_url, headers=headers)
if r.status_code == codes.ok:
    print(r.json())
else:
    print(r.status_code)