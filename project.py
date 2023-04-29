from worldbankapi import WorldBankAPI
from countrieswb import CountriesAtWBAPI
import pandas as pd

if __name__ == "__main__":
    countries = CountriesAtWBAPI().get_countries()
    #countries=[('United States','US'), ('Mexico', 'UY'), ('Togo','TZ'), ('Yemen', 'YE')]

    n = 0
    for country in countries:
        n += 1
        print('Datos de', country[0], 'listos')
        api = WorldBankAPI(country[1],country[0])
        df = api.get_all_data(country[1],country[0])
        if n == 9:
            print("Se ha alcanzado el valor máximo para esta prueba:", n, 'países')
            break
