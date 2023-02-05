import sqlite3 as sl

# connect to database
conn = sl.connect('database.db')

# create a cursor
c = conn.cursor()

# c.execute ("DROP TABLE users")
# c.execute ("DROP TABLE media")
# c.execute ("DROP TABLE reviews")

# c.execute (''' CREATE TABLE users (
#     userID INTEGER PRIMARY KEY AUTOINCREMENT,
#     username text NOT NULL,
#     password text NOT NULL
# )
#            ''')

# c.execute (''' CREATE TABLE media (
#     mediaID INTEGER PRIMARY KEY AUTOINCREMENT,
#     mediaName text NOT NULL,
#     mediaType text NOT NULL
# )
#            ''')

# c.execute (''' CREATE TABLE reviews (
#     reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
#     userID INTEGER NOT NULL,
#     mediaID INTEGER NOT NULL,
#     reviewTitle text NOT NULL,
#     reviewText text NOT NULL,
#     mediaType text NOT NULL,
#     yum TINYINT NOT NULL,
#     date NOT NULL
# )
#            ''')

# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh10', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh2', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh3', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh4', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh5', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh6', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh7', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh8', '1738nay')")
# c.execute("INSERT INTO users (username, password) VALUES ('bihyuh9', '1738nay')")
# # c.execute("SELECT * FROM users")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman1', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman2', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman3', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman4', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman5', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman6', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman7', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman8', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman9', 'movie')")
# c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman10', 'movie')")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (4, 1, 'MID','not a1', 'movie', 1, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (5, 5, 'MID','a banger2', 'movie',  0, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (1, 6, 'MID', 'not banger3', 'movie',  1, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (2, 10, 'MID', 'banger not4', 'movie',  0, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (6, 1, 'MID', 'not a5', 'movie',  1, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (3, 5, 'MID', 'a banger6', 'movie',  0, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (1, 6, 'MID', 'not banger7', 'movie',  1, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (7, 10, 'MID', 'banger not8', 'movie',  0, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (1, 6, 'MID', 'not banger9', 'movie',  1, datetime('now', 'localtime'))")
# c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (9, 10, 'MID', 'banger not10', 'movie',  0, datetime('now', 'localtime'))")
c.execute("SELECT * FROM reviews")
# c.execute('''SELECT u.username
#                 FROM users u, reviews r
#                 Where u.userID = r.userID
#                 AND u.userID != 1
#                 ''')
for row in c:
    print("userID = ", row[1])
    print("mediaID = ", row[2])
    print("reviewTitle = ", row[3])
    print("reviewText = ", row[4])
    print("mediaType = ", row[5])
    if (row[6] == 1):
        print("yum")
    else:
        print("yuck")
    print("date: = ", row[7])
    

# c.execute("SELECT * FROM users")

conn.commit()

conn.close()
