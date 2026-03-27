"""
05_jsonplaceholder_delete_post.py
---------------------------------
Deletes an existing post using JSONPlaceholder (DELETE request).
"""

import requests

posts_url = 'https://jsonplaceholder.typicode.com/posts'
post_id_to_delete = 1
delete_url = f'{posts_url}/{post_id_to_delete}'

response = requests.delete(delete_url)

if response.status_code == 200:
    print(f'Post {post_id_to_delete} deleted successfully.')
    print(f'Response Status Code: {response.status_code}')
else:
    print(f'Failed to delete post: {response.status_code}')
