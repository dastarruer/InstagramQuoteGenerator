from requests import get

print(get("https://api.quotable.io/quotes/random").json())