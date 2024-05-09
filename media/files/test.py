import requests

responsess = requests.get('https://api.github.com')
print(responsess.status_code)