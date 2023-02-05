import sqlite3 as sl
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__, template_folder='templates', static_folder='static')


def db_list_review_return(int) -> list:
    conn = sl.connect("database.db")
    c = conn.cursor()
    d = c.execute("SELECT * FROM usersexample4 WHERE id!=?", (int,))
    #print(*d)
    review_list = []

    for data in d:
        review_list.append(data[3])
    review_list.reverse()
    conn.commit()
    return review_list



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
    # otherwise close connection and return false
    return False


def db_create_user(un: str, pw: str) -> None:
    conn = sl.connect("database.db")
    c = conn.cursor()
    v = (un,pw)
    c.execute("SELECT COUNT(*) FROM users WHERE username=?",(un,))
    result = c.fetchone()[0]
    if result == 0:
        stmnt1 = "INSERT INTO users (`username`, `password`) VALUES (?,?)"
        c.execute(stmnt1, v)
        conn.commit()
        print("execution worked added to users table")
    else:
        print("user already exists")
