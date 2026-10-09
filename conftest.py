import pytest
import requests


@pytest.fixture(scope="session")
def response():
    return requests.get("https://jsonplaceholder.typicode.com/posts")
    

@pytest.fixture(scope="session")
def posts(response):
    return response.json()