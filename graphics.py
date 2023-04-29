from worldbankapi import WorldBankAPI
import matplotlib.pyplot as plt

# Initialize the WorldBankAPI object
api = WorldBankAPI("US")

# Retrieve the data for a specific country
country_code = "US"
data = api.get_all_data(country_code)

# Plot the data
years = [item["date"] for item in data]
values = [item["value"] for item in data]
plt.plot(years, values)
plt.title(f"{country_code} Data")
plt.xlabel("Year")
plt.ylabel("Value")
plt.show()

