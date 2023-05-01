import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
        plt.show()

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
    plt.show()



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
        plt.show()

#Inflation vs FDI
class FDIInflationChart:
    def __init__(self, data, country, start_year, end_year):
        self.data = data
        self.country = country
        self.start_year = start_year
        self.end_year = end_year
        self.years = [str(year) for year in range(self.start_year, self.end_year+1)]
        
    def plot(self):
        fig, ax = plt.subplots()
        for year in self.years:
            df = self.data[self.data['Year'] == year]
            if not df.empty:
                ax.scatter(df['Inflation, consumer prices (annual %)'], df['Foreign direct investment, net inflows (% of GDP)'], label=year)
        ax.set_xlabel('Inflation (%)')
        ax.set_ylabel('FDI (% of GDP)')
        ax.set_title(f'{self.country} - FDI vs Inflation ({self.start_year}-{self.end_year})')
        if len(ax.lines) > 0:
            ax.legend()
            plt.show()
        else:
            print(f"No data found for {self.country} in the given time range.")






