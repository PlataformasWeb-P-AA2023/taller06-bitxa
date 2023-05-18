import requests

url = 'https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json'

def get_data():
    data = requests.get(url)
    return data.json()
    