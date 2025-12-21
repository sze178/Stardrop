# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

from flask import Flask, render_template, request, flash, redirect, session, url_for
import sqlite3, json
from db import *

from game_state import *
from recipes import *

GoldAPIKey = "" #KEY HERE

app = Flask(__name__)
app.secret_key = "zxlkcvjlxzkjvlxcjlk"

@app.get("/")
def index_get():
    try:
        keyfile = open("keys/xkey_GoldAPI.txt")
        GoldAPIKey = next(keyfile)
        print(GoldAPIKey)
    except FileNotFoundError:
        print("NO GOLD API KEY FILE AVAILABLE")
        flash("No GOLD API key file available", "error")
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
    insert_query("players", {"username": username, "password": password})
    flash("Account successfully registered. Please log in.", "success")
    initialize_supplies(username) # not entirely sure if this should go here
    return redirect(url_for("login_get"))

@app.get('/logout')
def logout_get():
    session.pop('username', None)
    flash("You are now logged out.", "success")
    return redirect(url_for("index_get"))

@app.get('/settings')
def settings_get():
    return render_template("settings.html")

@app.get('/game_scene')
def game_scene_get():
    date = "11/23/2023"
    coords = request_coordinates(date_to_timestamp(date))
    coords[0] = round(coords[0], 4)
    coords[1] = round(coords[1], 4)
    if "username" not in session.keys():
        flash("Please log in or register first.", "error")
        return redirect(url_for("index_get"))
    seat_number = request.args.get("seat_number")
    drink_name=""
    ingredients = []
    # print(select_query("SELECT supplies FROM players WHERE username=?", [session["username"]]))
    supplies=json.loads(select_query("SELECT supplies FROM players WHERE username=?", [session["username"]])[0]["supplies"])
#    print(supplies.keys())
#    print(list(supplies.keys()))
#    print(list(supplies.keys()))
    alphabetical_supplies=sorted(list(supplies.keys()))
    quantities=[]
    npc = ""
    npc_data = {}
    for item in alphabetical_supplies:
        quantities.append(supplies[item])
    if seat_number:
        npc = npc_at_seat[int(seat_number) - 1]
        session["npc"]=npc
        npc_data = get_npc_drink_preferences(npc)
        for i in range(3):
            npc_data[list(npc_data)[i]]=list(npc_data.values())[i].capitalize()
        drink_id = npc_drink_order(npc)
        drink = request_drink(drink_id)
        session["drink"] = drink
        set_last_order(drink, npc)
        ingredients = drink["ingredients"] 
        drink_name = drink["drink"]
    results=session.get("results", False)
    if results:
        session.pop("results")
    return render_template(
        "game_scene.html", 
        order=(seat_number is not None), 
        drink_name=drink_name, 
        ingredients=ingredients, 
        supplies=alphabetical_supplies, 
        quantities=quantities, 
        npc=npc,
        npc_data=npc_data,
        results=results
    )

@app.post("/order")
def take_order():
    return redirect(url_for("game_scene_get", seat_number=request.form.get("seat_number")))

@app.post("/make_drink")
def make_drink():
    added_ingredients = {}
    supplies=json.loads(select_query("SELECT supplies FROM players WHERE username=?", [session["username"]])[0]["supplies"])
    alphabetical_supplies=sorted(list(supplies.keys()))
    # print(len(alphabetical_supplies))
    # print(len(get_all_ingredients()))
    for i in range(len(get_all_ingredients())):
        print(request.form.get(str(i)))
        if (request.form.get(str(i)) != "none"):
            added_ingredients[alphabetical_supplies[i]] = request.form.get(str(i))
    session["results"] = calculate_results(session.get("npc"), session.get("drink"), added_ingredients)
    # check_stock(added_ingredients)
    # update_stock(added_ingredients, -1)
    return redirect(url_for("game_scene_get"))

if __name__ == "__main__":
    app.debug = True
    app.run()