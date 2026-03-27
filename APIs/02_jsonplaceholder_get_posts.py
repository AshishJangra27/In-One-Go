"""
02_jsonplaceholder_get_posts.py
------------------------------
Fetches a list of posts from JSONPlaceholder and prints the first 5 post titles.
"""

import requests

posts_url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(posts_url)

if response.status_code == 200:
    posts = response.json()
    print(f'Successfully fetched {len(posts)} posts.')
    print('First 5 Post Titles:')
    for post in posts[:5]:
        print(f"- {post['title']}")
else:
    print(f'Failed to fetch posts: {response.status_code}')
