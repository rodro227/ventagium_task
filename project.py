from worldbankapi import WorldBankAPI
from countrieswb import CountriesAtWBAPI
from graphics import GDPChart, UnemploymentChart, PopulationChart, FDIInflationChart
import pandas as pd

if __name__ == "__main__":
    #countries = CountriesAtWBAPI().get_countries()
    countries=[('United States','US'), ('Mexico', 'MX'), ('Argentina','AR'), ('China', 'CN')]

    #List of dataframes
    dfs = []

    n = 0
    for country in countries:
        n += 1
        print('Datos de', country[0], 'listos')
        api = WorldBankAPI(country[1],country[0])
        df = api.get_all_data(country[1],country[0])
        dfs.append(df)
        if n == 9:
            print("Se ha alcanzado el valor máximo para esta prueba:", n, 'países')
            break
    
    df_all = pd.concat(dfs)
    #gdp_chart = GDPChart(df_all, 2016)
    #gdp_chart.plot()

    print(df.columns)
    #unemployment_chart = UnemploymentChart(df_all)
    #unemployment_chart.plot()

    #population_chart = PopulationChart(df_all)
    #population_chart.plot()

    chart = FDIInflationChart(df_all, 'United States', 2000, 2020)
    chart.plot()
