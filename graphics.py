import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Circular chart for global population distribution
class PopulationChart:
    def __init__(self, df):
        self.df = df
        
    def plot(self):
        # Sum the population for each country
        total_population = self.df.groupby('Country')['Population, total'].sum()
        
        # Create the pie chart
        fig, ax = plt.subplots()
        ax.pie(total_population, labels=total_population.index, autopct='%1.1f%%')
        ax.set_title('Population distribution by country')
        plt.savefig('charts/population_chart.png')
        #plt.show()

# Bar Chart of the GPD of each country
class GDPChart:
    def __init__(self, df, start_year):
        self.df = df[df['Year'] >= start_year]
        self.start_year = start_year
    
def plot(self):
    print('Data:', self.data)
    print('Years:', self.years)
    print('Country:', self.country)
    fig, ax = plt.subplots()
    for year in self.years:
        df = self.data[self.data['Year'] == year]
        ax.scatter(df['Inflation, consumer prices (annual %)'], df['Foreign direct investment, net inflows (% of GDP)'], label=year)
    ax.set_xlabel('Inflation (%)')
    ax.set_ylabel('FDI (% of GDP)')
    ax.set_title(f'{self.country} - FDI vs Inflation ({self.start_year}-{self.years[-1]})')
    ax.legend()
    #plt.show()



#Line chart of the unemployment of each country per year

class UnemploymentChart:
    def __init__(self, data):
        self.df = data
    
    def plot(self):
        fig, ax = plt.subplots()
        for country in self.df['Country'].unique():
            country_data = self.df[self.df['Country'] == country]
            ax.plot(country_data['Year'], country_data['Unemployment, total (% of total labor force) (modeled ILO estimate)'].astype(float), label=country)
        ax.set_xlabel('Year')
        ax.set_ylabel('Unemployment rate (%)')
        ax.set_title('Unemployment rates by country')
        ax.legend(loc='upper left')
        plt.savefig('charts/unemployment_chart.png')
        #plt.show()

#Inflation vs FDI scatter plot

class FDIInflationChart:
    def __init__(self, df, country, start_year=2000):
        self.df = df
        self.country = country.title()

        self.start_year = start_year
        self.years = [y for y in range(start_year, 2022) if y in df.loc[df['Country'] == country, 'Year'].values]

    
    def plot(self):
        data = self.df.loc[(self.df['Country'] == self.country) & (self.df['Year'].isin(self.years)), :]
        if data.empty:
            print(f"No data found for {self.country}")
            return

        # Convertir FDI neto a dólares per cápita
        data['FDI, net inflows (BoP, current US$) per capita'] = data['Foreign direct investment, net inflows (% of GDP)'] * data['GDP per capita (current US$)'] / 100

        fig, ax = plt.subplots(figsize=(10, 6))
        ax = sns.scatterplot(data=data, x='Inflation, consumer prices (annual %)', y='FDI, net inflows (BoP, current US$) per capita', hue='Year', s=80, legend='full')
        ax.set_xlabel('Inflation, consumer prices (annual %)')
        ax.set_ylabel('Foreign direct investment, net inflows (BoP, current US$) per capita')
        ax.set_title(f'{self.country} - FDI vs Inflation ({self.start_year}-{self.years[-1]})')

        # Ajustar rango de los ejes
        x_min, x_max = data['Inflation, consumer prices (annual %)'].min(), data['Inflation, consumer prices (annual %)'].max()
        y_min, y_max = data['FDI, net inflows (BoP, current US$) per capita'].min(), data['FDI, net inflows (BoP, current US$) per capita'].max()
        x_padding = (x_max - x_min) * 0.1
        y_padding = (y_max - y_min) * 0.1
        ax.set_xlim([x_min - x_padding, x_max + x_padding])
        ax.set_ylim([y_min - y_padding, y_max + y_padding])
        
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8, markerscale=0.8)
        plt.savefig('charts/fdi_inflation_chart.png')
        #plt.show()
