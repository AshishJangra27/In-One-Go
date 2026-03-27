"""
03_jsonplaceholder_create_post.py
--------------------------------
Creates a new post using JSONPlaceholder (POST request).
"""

import requests

posts_url = 'https://jsonplaceholder.typicode.com/posts'

new_post = {
    'title': 'Learning REST APIs',
    'body': 'This post was created using a POST request in Python.',
    'userId': 12
}

response = requests.post(posts_url, json=new_post)

if response.status_code == 201:
    created_post = response.json()
    print('Post created successfully!')
    print(f"ID: {created_post['id']}")
    print(f"Title: {created_post['title']}")
else:
    print(f'Failed to create post: {response.status_code}')
