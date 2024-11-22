from api import API_NINJAS_KEY

from requests import get, codes


class QuoteGenerator:
    def generate_quote(self, category):
        """
        Generate a quote using the API Ninjas Quotes API.
        """
        headers = {
            'X-Api-Key':API_NINJAS_KEY
        }
        api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'

        quote = get(api_url, headers=headers)
        if quote.status_code == codes.ok:
            quote = quote.json()[0]
            return (quote["quote"], quote["author"])
        print(f"Something went wrong... ({quote.status_code})")
        
        
quote_generator = QuoteGenerator()
