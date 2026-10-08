import requests

def test_can_get_posts():
    response =  requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200