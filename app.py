import requests

def GetHyrule(compendium):
    response = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{compendium.lower()}')
    if response.status_code != 200:
        print ('Error fetching data')
        return None
    
    data = response.json()
    return {
        "name": data['name'],
        "id": data["id"],
        "category": data["category"],
        "decription": data['description']
     }


hyrule = GetHyrule("horse")
print(hyrule)
# url = "https://botw-compendium.herokuapp.com/api/v3/compendium/all"

# response = requests.get(url)

# print(response.json())