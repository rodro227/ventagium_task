from module1 import WorldBankAPI

if __name__ == "__main__":
    api = WorldBankAPI("SP.POP.TOTL", "all")
    df = api.get_data()
    print(df.head())