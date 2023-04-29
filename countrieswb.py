import requests

class CountriesAtWBAPI:
    def __init__(self):
        self.url = "https://api.worldbank.org/v2/countries?per_page=500&format=json"
    
    def get_countries(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            countries = [(c['name'], c['iso2Code']) for c in data[1]]
            return countries
        else:
            return "Error:", response.status_code








    