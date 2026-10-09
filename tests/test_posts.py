import requests


def test_can_get_posts(response):
    assert response.status_code == 200

def test_posts_returns_100_posts_with_expected_fields(posts):
    assert len(posts) == 100
    key_names = ["id", "title", "body", "userId"]
    for post in posts:
        for name in key_names:
            assert name in post, f"{name} not in {post}"
            