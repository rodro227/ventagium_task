from worldbankapi import WorldBankAPI
#from countrieswb import CountriesAtWBAPI
import pandas as pd

if __name__ == "__main__":
    #countries = CountriesAtWBAPI().get_countries()
    countries=[('United States','US'), ('Mexico', 'UY')]
    print(countries)
    for country in countries:
        print(country)
        api = WorldBankAPI(country[1],country[0])
        df = api.get_all_data(country[1],country[0])