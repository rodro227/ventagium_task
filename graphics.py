import pandas as pd
import matplotlib.pyplot as plt

# Bar Chart of the GPD of each country
class GDPChart:
    def __init__(self, df):
        self.df = df
        
    def plot(self):
        plt.bar(self.df['Country'], self.df['GDP per capita (current US$)'])
        plt.xticks(rotation=90)
        plt.ylabel('GDP per capita (current US$)')
        plt.title('GPD (Gross domestic product)')
        plt.show()
