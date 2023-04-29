from module1_2 import WorldBankAPI
import pandas as pd

Country = "USA"

if __name__ == "__main__":
    api = WorldBankAPI(Country)
    #api = WorldBankAPI()
    df = api.get_all_data(Country)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #print(df.head())
    #print(df)