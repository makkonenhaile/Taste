import sqlite3 as sl

# connect to database
conn = sl.connect('database.db')

# create a cursor
c = conn.cursor()

c.execute ("DROP TABLE users")
c.execute ("DROP TABLE media")
c.execute ("DROP TABLE reviews")

c.execute (''' CREATE TABLE users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username text NOT NULL,
    password text NOT NULL,
    image text
)
           ''')

c.execute (''' CREATE TABLE media (
    mediaID INTEGER PRIMARY KEY AUTOINCREMENT,
    mediaName text NOT NULL,
    mediaType text NOT NULL
)
           ''')

c.execute (''' CREATE TABLE reviews (
    reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    mediaID INTEGER NOT NULL,
    reviewTitle text NOT NULL,
    reviewText text NOT NULL,
    mediaType text NOT NULL,
    yum TINYINT NOT NULL,
    date NOT NULL
)
           ''')

c.execute("INSERT INTO users (username, password, image) VALUES ('Ardern', '1738nay', 'images/headshot1.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Cypress', '1738nay', 'images/headshot2.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Hollis', '1738nay', 'images/headshot3.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Kit', '1738nay', 'images/headshot4.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Revel', '1738nay', 'images/headshot5.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Rory', '1738nay', 'images/headshot6.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Jessie', '1738nay', 'images/headshot7.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Jamie', '1738nay', 'images/headshot8.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Jackie', '1738nay', 'images/headshot9.jpg')")
c.execute("INSERT INTO users (username, password, image) VALUES ('Frankie', '1738nay', 'images/headshot10.jpg')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Superman', 'movie')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Folklore', 'music')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Batman', 'movie')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('The Mona Lisa', 'art')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('McDonalds', 'food')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Burger King', 'food')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('The Forever Story', 'music')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Friends', 'tv')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Naruto', 'anime')")
c.execute("INSERT INTO media (mediaName, mediaType) VALUES ('Hyperdunks', 'fashion')")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (1, 1, 'Astonishing!','He be flying!', 'movie', 1, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (2, 5, 'Eh','1989 is better', 'music',  0, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (3, 6, 'Great!', 'He do not be flying but he is rich and his tools are so sick', 'movie', 1, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (4, 10, 'Mid', 'She was not even that fly', 'art',  0, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (5, 1, 'Solid', 'Burger', 'food',  1, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (6, 5, 'Ok', 'Burger but not very good', 'food',  0, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (7, 6, 'Worth the Hype', 'Loved this album', 'music',  1, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (8, 10, 'Not Worth the Hype', 'What is their deal?', 'tv',  0, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (9, 7, 'Would watch again', 'I have seen this show before definitely', 'anime',  1, datetime('now', 'localtime'))")
c.execute("INSERT INTO reviews (userID, mediaID, reviewTitle, reviewText, mediaType, yum, date) VALUES (10, 10, 'Not a fan', 'Shoes but not really fo me', 'fashion',  0, datetime('now', 'localtime'))")
c.execute("SELECT * FROM users")
# c.execute('''SELECT u.username
#                 FROM users u, reviews r
#                 Where u.userID = r.userID
#                 AND u.userID != 1
#                 ''')
for row in c:
    print("userID = ", row[0])
    print("username = ", row[1])
    print("password = ", row[2])
    print("password = ", row[3])
    

# c.execute("SELECT * FROM users")

conn.commit()

conn.close()
