import requests

def test_db_works(db):
    db.execute("""INSERT INTO posts (id, userId, title, body)
        VALUES (?, ?, ?, ?)
        """, (1, 1, "test_title", "test_body"))
    row = db.execute("""SELECT title FROM posts WHERE id = ?""", (1,)).fetchone()
    assert row[0] == "test_title"

