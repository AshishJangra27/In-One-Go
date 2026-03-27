"""
06_restcountries_get_country.py
------------------------------
Fetches country data from the REST Countries API and prints the name and population.
"""

import requests

country_name_url = 'https://restcountries.com/v3.1/name/usa'

try:
    country_resp = requests.get(country_name_url, timeout=10)
    if country_resp.status_code == 200:
        usa_data = country_resp.json()[0]
        name = usa_data.get('name', {}).get('common')
        pop = usa_data.get('population')
        print(f'Country Data Found: {name} - {pop:,} residents\n')
    else:
        print(f'REST Countries API unavailable (Status {country_resp.status_code}).')
except Exception as e:
    print(f'Country API error: {e}')
