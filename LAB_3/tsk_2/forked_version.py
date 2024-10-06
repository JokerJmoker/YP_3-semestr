import requests

params = {'q': 'joker'}

response = requests.get('https://www.google.com/search', params=params)

print(response.text)