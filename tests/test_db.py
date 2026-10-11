import requests

def test_db_works(db):
    db.execute("""INSERT INTO posts (id, userId, title, body)
        VALUES (?, ?, ?, ?)
        """, (1, 1, "test_title", "test_body"))
    row = db.execute("""SELECT title FROM posts WHERE id = ?""", (1,)).fetchone()
    assert row[0] == "test_title"

def test_db_builds_list_of_100_tuples(db, posts):
    #key_names = ["id", "userId", "title", "body"]
    #first = (post["id"], post["userId"], post["title"], post["body"])
    db_list = []
    for post in posts:
        post_tuple = (post["id"], post["userId"], post["title"], post["body"])
        db_list.append(post_tuple)
    print(len(db_list))    




#city = {"id": 1, "city": "Columbus", "state": "OH"}
#row = (city["id"], city["city"], city["state"])
