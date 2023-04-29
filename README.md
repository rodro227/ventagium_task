# ventagium_task
#Activar entorno virtual
source env/bin/activate
#Checar si pip está in-day
python3 -m pip install --upgrade pip

The class WorldBankAPI() recieves the country code to work.
It contains several methods that allows us to consult the following indicators about the country given as the parameter.

To consult the population use:
get_population(country_code)

To consult the Gross Domestic Product (GPD) use:
get_gdp_per_capita(country_code)

To consult the health expenditure per capita use:
get_health_exp_per_capita(country_code)

To consult the inflation rate per year  use:
get_inflation(self, country_code)

To consult the unamployment (% of total labor force) use:
get_unemployment(country_code)

To consult the Foreign Direct Investment (FDI) use:
get_fdi_data(country_code)