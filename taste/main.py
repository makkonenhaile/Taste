import sqlite3 as sl
from flask import Flask, render_template, request, url_for, redirect, session
from flask_session import Session

def get_db_connection():
    conn = sl.connect('database.db')
    conn.row_factory = sl.Row
    return conn

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.config['SECRET_KEY'] = 'secretkey123'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def db_create_user(un: str, pw: str) -> bool:
    conn = sl.connect("database.db")
    c = conn.cursor()
    v = (un,pw)
    c.execute("SELECT COUNT(*) FROM users WHERE username=?",(un,))
    result = c.fetchone()[0]
    if result == 0:
        return True
    else:
        return False


def db_check_creds(un: str, pw: str) -> bool:
    conn = sl.connect("database.db")
    c = conn.cursor()
    # getting username and password
    v = (un,pw)
    # getting data from
    x = ("""SELECT * FROM users WHERE `username`=? AND `password` =?""")
    data = c.execute(x,v)
    conn.commit()
    if not data:
        #conn.close()
        return False
    # if there is data return True and close connection
    for r in data:
        #conn.close()
        return True
    return False

@app.route('/')
def homepage():
    return render_template('homepage.html') 

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form['password']
        if db_check_creds(username, password) == True:
            # User is valid, proceed to their homepage or wherever they need to go
            conn = sl.connect("database.db")
            c = conn.cursor()
            session["username"] = username
            idColumn = c.execute("SELECT userID FROM users WHERE username = ?", (username,)).fetchone()
            session["id"] = idColumn[0]
            conn.close()
            print(session["id"])
            return redirect('/truefeed')
        else:
            # User is not valid, show error message
            return render_template('login.html', error='Invalid credentials')
    return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    conn = sl.connect("database.db")
    c = conn.cursor()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form['password']
        confirmedPassword = request.form['password_again']
        v = (username, password, 'images/default.jpg')
        b = db_create_user(username,password)
        if b:
            if password == confirmedPassword:
                stmnt1 = "INSERT INTO users (`username`, `password`, `image`) VALUES (?,?,?)"
                c.execute(stmnt1, v)
                conn.commit()
                session["username"] = username
                idColumn = c.execute("SELECT userID FROM users WHERE username = ?", (username,)).fetchone()
                session["id"] = idColumn[0]
                conn.close()
                print(session["id"])
                return redirect('/truefeed')
            else:
                return render_template('signup.html', error='Invalid credentials')
        else:
            return render_template('signup.html', error='Invalid credentials')
    return render_template("signup.html")

@app.route('/truefeed')
def truefeed():
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews WHERE userID != ? ORDER BY reviewID DESC', (session["id"],)).fetchall()
    conn.row_factory = lambda cursor, row: row[0]
    usernames = conn.execute('''SELECT u.username
                            FROM users u, reviews r
                            Where u.userID = r.userID
                            AND u.username != ?
                            ''', (session["username"],)).fetchall()
    images = conn.execute('''SELECT u.image
                            FROM users u, reviews r
                            Where u.userID = r.userID
                            AND u.username != ?
                            ''', (session["username"],)).fetchall()
    conn.close()
    return render_template('truefeed.html', reviews=reviews, usernames=usernames, user=session["username"], images=images) 

@app.route('/trueprofile')
def trueprofile():
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews WHERE userID = ? ORDER BY reviewID DESC', (session["id"],)).fetchall()
    conn.row_factory = lambda cursor, row: row[0]
    usernames = conn.execute('''SELECT u.username
                            FROM users u, reviews r
                            Where u.userID = r.userID
                            AND u.username = ?
                            ''', (session["username"],)).fetchall()
    images = conn.execute('''SELECT u.image
                            FROM users u, reviews r
                            Where u.userID = r.userID
                            AND u.username = ?
                            ''', (session["username"],)).fetchall()
    conn.close()
    return render_template('trueprofile.html', reviews=reviews, usernames=usernames, user=session["username"], images=images) 

@app.route("/logout")
def logout():
    session["name"] = None
    session["id"] = None
    return redirect("/")