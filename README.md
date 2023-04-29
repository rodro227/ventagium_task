# ventagium_task

<details><summary>General Notes</summary>
<p>

## Activar entorno virtual y checar si pip está up-to-day
```
source env/bin/activate
python3 -m pip install --upgrade pip
```
</p>
</details>

<details><summary>Description of worldbankapi.py</summary>
<p>

## WorldBankAPI class
This file contains the WorldBankAPI class to connect to The World Bank API that allows for the search and retrieval of the public, Bank documents available in the Documents & Reports site.  Records can be retrieved in a format useful for research and for inclusion in web sites outside of Documents & Reports and the World Bank. To read more about it, visit [World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)

## Methods of the World Bank API cass
The class WorldBankAPI() recieves the country code to work.
It contains several methods that allows us to consult the following indicators about the country given as the parameter.

1. To consult the population use:
´´´
get_population(country_code)
´´´

2. To consult the Gross Domestic Product (GPD) use:
´´´
get_gdp_per_capita(country_code)
´´´

3. To consult the health expenditure per capita use:
´´´
get_health_exp_per_capita(country_code)
´´´

4. To consult the inflation rate per year  use:
´´´
get_inflation(self, country_code)
´´´

5. To consult the unamployment (% of total labor force) use:
´´´
get_unemployment(country_code)
´´´

6. To consult the Foreign Direct Investment (FDI) use:
´´´
get_fdi_data(country_code)
´´´
</p>
</details>