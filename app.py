import requests

url = "https://botw-compendium.herokuapp.com/api/v3/compendium/all"

response = requests.get(url)

print(response.json())