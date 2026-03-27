# API Python Demo Scripts

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sFCIX8zAXa1vLzCx-hsHu-w3aCr7c4mL?usp=sharing)

**Colab Notebook:** [https://colab.research.google.com/drive/1sFCIX8zAXa1vLzCx-hsHu-w3aCr7c4mL?usp=sharing](https://colab.research.google.com/drive/1sFCIX8zAXa1vLzCx-hsHu-w3aCr7c4mL?usp=sharing)

# API Python Demo Scripts

This project demonstrates how to interact with various public APIs using Python and the requests library, progressing from basic to advanced concepts.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Scripts Overview

1. **01_agify_predict_age.py** — Agify API: Predict age based on a name (GET)
2. **02_jsonplaceholder_get_posts.py** — Fetch a list of posts from JSONPlaceholder (GET)
3. **03_jsonplaceholder_create_post.py** — Create a new post on JSONPlaceholder (POST)
4. **04_jsonplaceholder_update_post.py** — Update an existing post on JSONPlaceholder (PUT)
5. **05_jsonplaceholder_delete_post.py** — Delete a post on JSONPlaceholder (DELETE)
6. **06_restcountries_get_country.py** — Fetch country data from REST Countries API
7. **07_jokeapi_random_joke.py** — Fetch a random joke from Official Joke API
8. **08_openmeteo_weather.py** — Fetch current weather from Open-Meteo API with error handling
9. **09_coingecko_bitcoin_price_retry.py** — Fetch Bitcoin price from CoinGecko with retry logic
10. **10_jsonplaceholder_pagination.py** — Demonstrate pagination with JSONPlaceholder

Each script is self-contained and well-documented. Run them with:

```bash
python <script_name.py>
```

## Learn More
- Agify API docs: https://agify.io/
- JSONPlaceholder docs: https://jsonplaceholder.typicode.com/
- REST Countries docs: https://restcountries.com/
- Official Joke API: https://official-joke-api.appspot.com/
- Open-Meteo API: https://open-meteo.com/
- CoinGecko API: https://www.coingecko.com/en/api
- Python requests docs: https://docs.python-requests.org/
