from flask import Flask, render_template, request, flash, redirect, session, url_for
import sqlite3
from db import select_query, insert_query, general_query

GoldAPIKey = ""

try:
    keyfile = open("keys/key_GoldAPI.txt")
    GoldAPIKey = next(keyfile)
except FileNotFoundError:
    print("NO GOLD API KEY FILE AVAILABLE")

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
app.secret_key = "zxlkcvjlxzkjvlxcjlk"

@app.get("/")
def index_get():
    return render_template('index.html')


@app.get("/login")
def login_get():
    return render_template('login.html')


@app.post("/login")
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    ## print(select_query("SELECT * FROM players WHERE username=?", [username]))
    registered = select_query("SELECT * FROM players WHERE username=?", [username])
    if len(registered) == 0 or registered[0]["password"] != password:
        flash("Invalid credentials", "error")
        ## print("XXXXXXX")
        return redirect(url_for("login_get"))
    session["username"] = username
    return redirect(url_for("index_get")) 


@app.get("/register")
def register_get():
    return render_template("register.html")


@app.post("/register")
def register_post():
    username = request.form.get("username")
    password = request.form.get("password")
    registered = select_query("SELECT * FROM PLAYERS WHERE username=?", [username])
    if len(registered) != 0:
        flash("Username already exists", "error")
        return redirect(url_for("register_get"))
    print(insert_query("players", {"username": username, "password": password}))
    flash("Account successfully registered", "success")
    return redirect(url_for("login_get"))


if __name__ == "__main__":
    app.debug = True
    app.run()

