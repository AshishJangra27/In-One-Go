"""
07_jokeapi_random_joke.py
------------------------
Fetches a random joke from the Official Joke API and prints the setup and punchline.
"""

import requests

joke_url = 'https://official-joke-api.appspot.com/random_joke'
headers = {'Accept': 'application/json'}

joke_response = requests.get(joke_url, headers=headers)

if joke_response.status_code == 200:
    joke_data = joke_response.json()
    setup = joke_data.get('setup')
    punchline = joke_data.get('punchline')
    print('--- Random Joke ---')
    print(f'Setup: {setup}')
    print(f'Punchline: {punchline}')
else:
    print(f'Failed to fetch joke: {joke_response.status_code}')
