"""
04_jsonplaceholder_update_post.py
---------------------------------
Updates an existing post using JSONPlaceholder (PUT request).
"""

import requests

posts_url = 'https://jsonplaceholder.typicode.com/posts'
post_id = 1
update_url = f'{posts_url}/{post_id}'

updated_data = {
    'id': 1,
    'title': 'Updated Title: Mastering REST APIs',
    'body': 'This content has been updated using a PUT request.',
    'userId': 1
}

response = requests.put(update_url, json=updated_data)

if response.status_code == 200:
    updated_post = response.json()
    print(f'Post {post_id} updated successfully!')
    print(f"New Title: {updated_post['title']}")
    print(f"New Body: {updated_post['body']}")
else:
    print(f'Failed to update post: {response.status_code}')
