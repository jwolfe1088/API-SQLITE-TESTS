import requests

def test_can_get_posts():
    response =  requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

def test_posts_returns_100_posts_with_expected_fields():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    assert len(posts) == 100
    assert "id" in posts[0]
    assert "title" in posts[0]
    assert "body" in posts[0]
    assert "userId" in posts[0]