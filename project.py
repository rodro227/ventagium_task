from worldbankapi import WorldBankAPI
from countrieswb import CountriesAtWBAPI
from tester import CodeTester
from graphics import GDPChart, UnemploymentChart, PopulationChart, FDIInflationChart
import pandas as pd

if __name__ == "__main__":

    #Decide if you want to use all the countries or only MX, AR or CN
    while True:
        print('Type ´A´ if you want to run for all the countries or ´T´ to run a test with 3 countries')
        answer1 = input()
        if answer1 == 'A':
            countries = CountriesAtWBAPI().get_countries()
            break
        elif answer1 == 'T':
            countries=[('Mexico', 'MX'), ('Argentina','AR'), ('China', 'CN')]
            break
        else:
            print('invalid option')
    
    #Initializing some variables 
    dfs = []
    n = 0
    pt = CodeTester()

    #Starting the test
    pt.start()

    for country in countries:
        n += 1
        api = WorldBankAPI(country[1],country[0])
        df = api.get_all_data(country[1],country[0])
        dfs.append(df)
        print('Data of', country[0], 'ready')
        if n == 9:
            print("Se ha alcanzado el valor máximo para esta prueba:", n, 'países')
            break

    df_all = pd.concat(dfs)

    #Ending test
    pt.end()
    print()

    #Generates multiple bar tables from 2016 to the last year with info
    print('Generating GDP chart...')
    pt.start()
    gdp_chart = GDPChart(df_all, 2016)
    print('GDP chart generated, printing time and memory...')
    pt.end()
    print()
    gdp_chart.plot()

    #print(df.columns)

    #Generates the unemployment rate by year line chart
    print('Generating unemployment chart...')
    pt.start()
    unemployment_chart = UnemploymentChart(df_all)
    print('Unemployment chart generated, printing time and memory...')
    pt.end()
    print()
    unemployment_chart.plot()

    #Generates the Population circle graph
    print('Generating population chart...')
    pt.start()
    population_chart = PopulationChart(df_all)
    print('Population chart generated, printing time and memory...')
    pt.end()
    print()
    population_chart.plot()
    
    #print(df_all.info())
    #print(df.index.unique())

    #Generates the FDI vs Inflation scatter plot
    print('Generating FDI vs Inflation chart...')
    pt.start()
    chart = FDIInflationChart(df_all, 'Mexico')
    print('FDI vs Inflation chart generated, printing time and memory...')
    pt.end()
    print()
    chart.plot()
