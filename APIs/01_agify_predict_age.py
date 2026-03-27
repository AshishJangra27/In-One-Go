"""
01_agify_predict_age.py
----------------------
Demonstrates a GET request to the Agify API to predict the age associated with a specific name using query parameters.
"""

import requests

name = 'michael'
agify_url = f'https://api.agify.io?name={name}'

response = requests.get(agify_url)
if response.status_code == 200:
    data = response.json()
    print(f"Agify Prediction for '{name}':")
    print(f"Name : {data.get('name')}")
    print(f"Predicted Age: {data.get('age')}")
    print(f"Count: {data.get('count')}")
else:
    print(f'Failed to retrieve data: {response.status_code}')
