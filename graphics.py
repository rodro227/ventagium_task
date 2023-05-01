import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
"""
# Bar Chart of the GPD of each country
class GDPChart:
    def __init__(self, df, year):
        self.df = df[df['Year'] == year]
        
    def plot(self):
        plt.bar(self.df['Country'], self.df['GDP per capita (current US$)'])
        plt.xticks(rotation=90)
        plt.ylabel('GDP per capita (current US$)')
        plt.title(f'GPD (Gross domestic product) - Year {self.df.iloc[0]["Year"]}')
        plt.savefig('charts/gpd_chart.png')
        plt.show()
"""
class GDPChart:
    def __init__(self, df, start_year):
        self.df = df[df['Year'] >= start_year]
        self.start_year = start_year
    
    def plot(self):
        years = self.df['Year'].unique()
        n_years = len(years)
        nrows = int(np.ceil(n_years/2))
        
        fig, axs = plt.subplots(nrows=nrows, ncols=2, figsize=(12, 4*nrows))
        axs = axs.ravel()
        
        for i, year in enumerate(years):
            ax = axs[i]
            year_df = self.df[self.df['Year']==year]
            ax.bar(year_df['Country'], year_df['GDP per capita (current US$)'])
            ax.set_xticklabels(year_df['Country'], rotation=90)
            ax.set_ylabel('GDP per capita (current US$)')
            ax.set_title(f'GPD (Gross domestic product) - {year}')
        
        plt.tight_layout()
        plt.savefig('charts/gpd_chart.png')
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












