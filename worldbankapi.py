import requests
import pandas as pd

class WorldBankAPI:
    def __init__(self, country_code, country_name):
        self.base_url = "http://api.worldbank.org/v2/"
        #self.indicator_code = indicator_code
        self.country_code = country_code
        self.country_name = country_name
        self.format = "json"
        
    def get_population(self, country_code):
        endpoint = f"country/{country_code}/indicator/SP.POP.TOTL"
        data = self._fetch_data(endpoint)
        return self._extract_data(data)
    
    def get_gdp_per_capita(self, country_code):
        endpoint = f"country/{country_code}/indicator/NY.GDP.PCAP.CD"
        data = self._fetch_data(endpoint)
        return self._extract_data(data)
    
    def get_health_exp_per_capita(self, country_code):
        endpoint = f"country/{country_code}/indicator/SH.XPD.CHEX.PC.CD"
        data = self._fetch_data(endpoint)
        return self._extract_data(data)

    
    def get_inflation(self, country_code):
        endpoint = f"country/{country_code}/indicator/FP.CPI.TOTL.ZG"
        data = self._fetch_data(endpoint)
        return self._extract_data(data)
    
    def get_unemployment(self, country_code):
        endpoint = f"country/{country_code}/indicator/SL.UEM.TOTL.ZS"
        data = self._fetch_data(endpoint)
        return self._extract_data(data)
    
    def get_fdi_data(self, country_code):
        endpoint = f"country/{country_code}/indicator/BX.KLT.DINV.WD.GD.ZS"
        data = self._fetch_data(endpoint)
        return self._extract_data(data)


    
    def _fetch_data(self, endpoint):
        url = f"{self.base_url}{endpoint}?format={self.format}"
        response = requests.get(url)
        data = response.json()
        if not data:
            print(f"No data for endpoint {endpoint}")
            return None
        return data

    
    def _extract_data(self, data):
        #print(data)
        if not data or len(data) < 2 or not data[1]:
            # No hay datos disponibles para este indicador
            return pd.DataFrame()
    
        indicator_name = data[1][0]["indicator"]["value"]
        country_name = data[1][0]["country"]["value"]
        years = [int(x["date"]) for x in data[1]]
        values = [float(x["value"]) if x["value"] is not None else None for x in data[1]]
        df = pd.DataFrame({"Year": years, indicator_name: values})
        df.set_index("Year", inplace=True)
        return df


    
    def get_all_data(self, country_code, country_name):
        population = self.get_population(country_code)
        gdp_per_capita = self.get_gdp_per_capita(country_code)
        health_exp = self.get_health_exp_per_capita(country_code)
        #print(health_exp.head())
        inflation = self.get_inflation(country_code)
        #print(inflation.head())
        unemployment = self.get_unemployment(country_code)
        fdi = self.get_fdi_data(country_code)
        #print(fdi.head())
        
        df = pd.concat([population, gdp_per_capita, health_exp, inflation, unemployment, fdi], axis=1, sort=True)
        df['Country'] = country_name
        df.to_csv(f'data/{country_name}.csv')
        
        return df

