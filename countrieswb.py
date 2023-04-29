import requests

url = "https://api.worldbank.org/v2/countries?per_page=500&format=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    countries = [(c['name'], c['iso2Code']) for c in data[1]]
    print(countries)
else:
    print("Error:", response.status_code)








    