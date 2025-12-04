from flask import Flask, render_template, request, flash, redirect, session, url_for
import sqlite3

DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript("""
CREATE TABLE IF NOT EXISTS players (
    username TEXT PK,
    name TEXT,
    password TEXT,
    money_earned REAL,
    npc_1_interact INTEGER DEFAULT 0,
    npc_2_interact INTEGER DEFAULT 0,
    
    time_period DATETIME,
    alcohol_on BOOLEAN DEFAULT TRUE
);
""")

c.executescript("""
CREATE TABLE IF NOT EXISTS ingredients (
    name TEXT PK,
    color TEXT,
    price REAL
);
""")

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template('index.html')

@app.get("/login")
def login_get():
    return render_template('login.html')

def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    registered = select_query("SELECT * IN players WHERE username=?", [username])
    if len(registered) = 0 or registered[1] != "password":
        flash("Invalid credentials")
        return redirect(url_for(login_get()))
    else:
        session["username"] = username
        return redirect(url_for(index_get())) 
