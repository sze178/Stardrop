# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

from flask import Flask, render_template, request, flash, redirect, session, url_for
import sqlite3, json
from db import *

from game_state import *
from recipes import *

app = Flask(__name__)
app.secret_key = "zxlkcvjlxzkjvlxcjlk"

@app.get("/")
def index_get():
    try:
        keyfile = open("keys/key_GoldAPI.txt")
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
    registered = select_query("SELECT * FROM players WHERE username=?", [username])
    if len(registered) != 0:
        flash("Username already exists", "error")
        return redirect(url_for("register_get"))
    insert_query("players", {"username": username, "password": password})
    flash("Account successfully registered. Please log in.", "success")
    initialize_supplies(username) 
    time_data = time_travel()
    print(time_data)
    session["date"] = time_data[0]
    general_query("UPDATE players SET date=? WHERE username=?", [time_data[0], username])
    general_query("UPDATE players SET conversion_rate=? WHERE username=?", [time_data[1]["price_gram_10k"], username])
    return redirect(url_for("login_get"))

@app.get('/logout')
def logout_get():
    session.clear()
    flash("You are now logged out.", "success")
    return redirect(url_for("index_get"))

@app.get('/settings')
def settings_get():
    alcohol_on = select_query("SELECT alcohol_on FROM players WHERE username=?", [session["username"]])[0]["alcohol_on"]
    return render_template("settings.html", alcohol_on=alcohol_on, username=session["username"])

@app.post("/toggle_alcohol")
def toggle_alcohol():
    current_setting=select_query("SELECT alcohol_on FROM players WHERE username=?", [session["username"]])[0]["alcohol_on"]
    general_query("UPDATE players SET alcohol_on=? WHERE username=?", [not current_setting, session["username"]])
    flash("Your alcohol preference has been changed", "success")
    return redirect(url_for("settings_get"))

@app.post("/change_username")
def change_username():
    new_username = request.form.get("username")
    for user in select_query("SELECT username FROM players"):
        if user["username"] == new_username:
            flash("This username is already taken", "error")
            return redirect(url_for("settings_get"))
    
    general_query("UPDATE players SET username=? WHERE username=?", [new_username, session["username"]])
    session["username"]=new_username
    flash(f"Your username has successfully been changed to {new_username}", "success")
    return redirect(url_for("settings_get"))

@app.post("/change_password")
def change_password():
    if request.form.get("old_password") != select_query("SELECT password FROM players WHERE username=?", [session["username"]])[0]["password"]:
        flash("Invalid current password entered", "error")
        return redirect(url_for("settings_get"))
    
    new_password = request.form.get("new_password")
    if new_password != request.form.get("reconfirm_password"):
        flash("Passwords do not match", "error")
        return redirect(url_for("settings_get"))
    
    general_query("UPDATE players SET password=? WHERE username=?", [new_password, session["username"]])
    flash("Your password has successfully been changed", "success")
    return redirect(url_for("settings_get"))

@app.get('/game_scene')
def game_scene_get():
    date = session.get("date", "11/21/2023")
    coords = request_coordinates(date)
    coords[0] = round(coords[0], 4)
    coords[1] = round(coords[1], 4)
    if "username" not in session.keys():
        flash("Please log in or register first", "error")
        return redirect(url_for("index_get"))
    seat_number = request.args.get("seat_number")
    drink_name=""
    ingredients = []
    supplies=json.loads(select_query("SELECT supplies FROM players WHERE username=?", [session["username"]])[0]["supplies"])
    alphabetical_supplies=sorted(list(supplies.keys()))
    quantities=[]
    npc = ""
    npc_data = {}
    money=select_query("SELECT money FROM players WHERE username=?", [session["username"]])[0]["money"]
    order=False
    session["santa_order"] = session.get("santa_order", False)
    session["cowboy_order"] = session.get("cowboy_order", False)
    session["pirate_order"] = session.get("pirate_order", False)
    for item in alphabetical_supplies: #builds quantity list for sidebar
        quantities.append(supplies[item])
    if seat_number and session.get("drink") is None: #take order
        npc = npc_at_seat[int(seat_number) - 1]
        session["npc"]=npc
        npc_data = get_npc_drink_preferences(npc)
        for i in range(3):
            npc_data[list(npc_data)[i]] = list(npc_data.values())[i].capitalize()
        drink_id = npc_drink_order(npc)
        drink = request_drink(drink_id)
        session["drink"] = drink
        ingredients = drink["ingredients"] 
        drink_name = drink["drink"]
        order=True
    elif session.get("drink") is not None: #reloading order after error
        npc = session.get("npc")
        npc_data = get_npc_drink_preferences(npc)
        for i in range(3):
            npc_data[list(npc_data)[i]] = list(npc_data.values())[i].capitalize()
        drink_name = session["drink"]["drink"]
        ingredients = session["drink"]["ingredients"]
        order=True
    results=session.get("results", False)
    if results:
        session.pop("results")
    restock=False
    price=session.get("price", [])
    qty_available=session.get("qty_available", [])
    if select_query("SELECT order_counter FROM players WHERE username=?", [session["username"]])[0]["order_counter"] >= 3:
        restock=True
        for item in alphabetical_supplies:
            if session.get("price") is None:
                price.append(get_price(select_query("SELECT conversion_rate FROM players WHERE username=?", [session["username"]])[0]["conversion_rate"], item))
            if session.get("qty_available") is None:
                qty_available.append(get_qty())
        session["qty_available"] = qty_available
        session["price"] = price
    return render_template(
        "game_scene.html", 
        country = coords,
        date = date, 
        order=order, 
        drink_name=drink_name, 
        ingredients=ingredients, 
        supplies=alphabetical_supplies, 
        quantities=quantities, 
        npc=npc,
        npc_data=npc_data,
        results=results,
        price=price,
        qty_available=qty_available,
        money=money,
        restock=restock,
        order_display = [not session["santa_order"], not session["pirate_order"], not session["cowboy_order"]]
    )

@app.post("/order")
def take_order():
    return redirect(url_for("game_scene_get", seat_number=request.form.get("seat_number")))

@app.post("/make_drink")
def make_drink():
    added_ingredients = {}
    supplies=json.loads(select_query("SELECT supplies FROM players WHERE username=?", [session["username"]])[0]["supplies"])
    alphabetical_supplies=sorted(list(supplies.keys()))
    for i in range(len(get_all_ingredients())):
        amount = request.form.get(str(i))
        if (amount != "0"):
            added_ingredients[alphabetical_supplies[i]] = int(amount)
    if not check_stock(session["username"], added_ingredients):
        flash("Not enough ingredients to make drink", "error")
        return redirect(url_for("game_scene_get"))
    change_stock(session["username"], added_ingredients, -1)
    results = calculate_results(session["username"], session.get("npc"), session.get("drink"), added_ingredients, select_query("SELECT conversion_rate FROM players WHERE username=?", [session["username"]])[0]["conversion_rate"])
    session["results"] = results
    opinion_change = 0
    if results[0] == "Terrible!":
        opinion_change = -2
    elif results[0] == "Could Be Better...":
        opinion_change = -1
    elif results[0] == "Wicked Drink!":
        opinion_change = 1
    elif results[0] == "Perfection!":
        opinion_change = 2
    general_query(f"UPDATE players SET {session.get('npc').lower()}_opinion = {session.get('npc').lower()}_opinion + ? WHERE username=?", [opinion_change, session["username"]])
    general_query("UPDATE players SET money = money + ? WHERE username=?", [round(results[1], 2), session["username"]])
    #print(select_query("SELECT * FROM players WHERE username=?", [session["username"]]))
    session[f"{session.get('npc').lower()}_order"] = True
    session.pop("drink")
    session.pop("npc")
    general_query("UPDATE players SET order_counter = order_counter + 1 WHERE username=?", [session["username"]])
    return redirect(url_for("game_scene_get"))

@app.post("/restock")
def restock():
    total_price=0
    bought_ingredients={}
    alphabetical_ingredients=sorted(list(get_all_ingredients()))
    for i in range(len(alphabetical_ingredients)):
        total_price += get_price(select_query("SELECT conversion_rate FROM players WHERE username=?", [session["username"]])[0]["conversion_rate"], alphabetical_ingredients[i]) * int(request.form.get(str(i)))
    if total_price > select_query("SELECT money FROM players WHERE username=?", [session["username"]])[0]["money"]:
        flash("Not enough money", "error")
        return redirect(url_for("game_scene_get"))
    general_query("UPDATE players SET money = money - ? WHERE username=?", [round(total_price, 2), session["username"]])
    for i in range(len(get_all_ingredients())):
        bought_ingredients[alphabetical_ingredients[i]] = request.form.get(str(i))
    change_stock(session["username"], bought_ingredients, 1)
    new_data = time_travel()
    session["date"] = new_data[0]
    general_query("UPDATE players SET date=? WHERE username=?", [new_data[0], session["username"]])
    general_query("UPDATE players SET conversion_rate=? WHERE username=?", [new_data[1]["price_gram_10k"], session["username"]])
    general_query("UPDATE players SET order_counter = 0 WHERE username=?", [session["username"]])
    session.pop("qty_available")
    session["santa_order"] = False
    session["cowboy_order"] = False
    session["pirate_order"] = False
    return redirect(url_for("game_scene_get"))

if __name__ == "__main__":
    app.debug = True
    app.run()