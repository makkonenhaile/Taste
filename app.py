import sqlite3 as sl
from flask import Flask, redirect, render_template, request, session, url_for, redirect

app = Flask(__name__, template_folder='templates', static_folder='static')

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
            return redirect('/')
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
        v = (username, password)
        b = db_create_user(username,password)
        if b:
            stmnt1 = "INSERT INTO users (`username`, `password`) VALUES (?,?)"
            c.execute(stmnt1, v)
            conn.commit()
            return redirect('/')
        else:
            return redirect('/login')

    return render_template("signup.html")




if __name__ == '__main__':
    app.run(port=5003, debug=True)






