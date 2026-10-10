import pytest
import requests
import sqlite3


@pytest.fixture(scope="session")
def response():
    return requests.get("https://jsonplaceholder.typicode.com/posts")
    

@pytest.fixture(scope="session")
def posts(response):
    return response.json()

@pytest.fixture(scope="function")#function is default but i added this for reference
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("""
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            title TEXT,
            body TEXT)
            """)
    yield conn
    conn.close()

