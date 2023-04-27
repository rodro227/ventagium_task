import requests
import pandas as pd

class WorldBankAPI:
    def __init__(self, indicator_id, iso2_code):
        self.base_url = "http://api.worldbank.org/v2/"
        self.endpoint = f"country/{iso2_code}/indicator/{indicator_id}"
        self.format = "json"
        
    def get_data(self):
        url = f"{self.base_url}{self.endpoint}?format={self.format}"
        response = requests.get(url)
        data = response.json()[1]
        df = pd.json_normalize(data)
        df = df[['country.value', 'date', 'value']]
        df.columns = ['Country', 'Year', 'Population']
        return df
    