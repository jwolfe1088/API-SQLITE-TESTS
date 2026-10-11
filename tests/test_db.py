import requests

def test_db_works(db):
    db.execute("""INSERT INTO posts (id, userId, title, body)
        VALUES (?, ?, ?, ?)
        """, (1, 1, "test_title", "test_body"))
    row = db.execute("""SELECT title FROM posts WHERE id = ?""", (1,)).fetchone()
    assert row[0] == "test_title"

def test_all_posts_stored_in_db(db, posts):
    db_list = []
    for post in posts:
        post_tuple = (post["id"], post["userId"], post["title"], post["body"])
        db_list.append(post_tuple)
    db.executemany("""INSERT INTO posts (id, userId, title, body)
        VALUES (?, ?, ?, ?)
        """, (db_list))
    count = db.execute("""SELECT COUNT(*) FROM posts""").fetchone()
    assert count[0] == 100
    first_title = db.execute("""SELECT title FROM posts WHERE id = ?""", (posts[0]["id"],)).fetchone()
    assert first_title[0] == posts[0]["title"]




#city = {"id": 1, "city": "Columbus", "state": "OH"}
#row = (city["id"], city["city"], city["state"])
