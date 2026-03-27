"""
10_jsonplaceholder_pagination.py
-------------------------------
Demonstrates pagination with JSONPlaceholder by fetching 10 posts from the second page.
"""

import requests

pagination_url = 'https://jsonplaceholder.typicode.com/posts'
params = {
    '_page': 2,
    '_limit': 10
}

try:
    response = requests.get(pagination_url, params=params)
    response.raise_for_status()
    paginated_posts = response.json()
    print(f'Successfully fetched {len(paginated_posts)} posts for Page 2 with a limit of 10:\n')
    print(f'{"ID":<5} | {"Title"}')
    print('-' * 40)
    for post in paginated_posts:
        title = post['title'][:50] + '...' if len(post['title']) > 50 else post['title']
        print(f"{post['id']:<5} | {title}")
except Exception as e:
    print(f'An error occurred during pagination request: {e}')
