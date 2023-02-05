import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.config['SECRET_KEY'] = 'secretkey123'

@app.route('/')
def index():
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews WHERE userID != 1').fetchall()
    conn.row_factory = lambda cursor, row: row[0]
    usernames = conn.execute('''SELECT u.username
                            FROM users u, reviews r
                            Where u.userID = r.userID
                            AND u.userID != 1
                           ''').fetchall()
    
    conn.close()
    return render_template('index.html', reviews=reviews, usernames=usernames)   

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')