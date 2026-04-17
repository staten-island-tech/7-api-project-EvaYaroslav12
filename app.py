import requests

def GetHyrule(compendium):
    response = requests.get(f'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{compendium.lower()}')
    if response.status_code != 200:
        print ('Error fetching data')
        return None

    data = response.json()
    return data

hyrule = GetHyrule(input('What do  you want to see? (Name or ID number) '))
print(hyrule['data']['name'])
print(hyrule['data']['id'])
print(hyrule['data']['category'])
print(hyrule['data']['description'])