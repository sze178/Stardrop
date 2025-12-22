# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

from recipes import *
from db import *
import random, json

alcoholOn = True
npc_at_seat = ["Santa", "Pirate", "Cowboy"]

#drink selections / list of ids from api to randomly choose from
#a if alcohol b if not
#1 fruity/sour
#2 milky/sweet
a1 = [58, 8603, 12212, 35427, 78945, 172502, 190753, 224615, 367321, 424489, 466077]
b1 = [43900, 357225, 499591, 627193, 778686, 805924]
a2 = [13554, 88538, 99612, 111282, 330969, 334642, 375884, 579225, 674837]
b2 = [42501, 264361, 434283, 577385, 934558]
#npcDrinkPreferences:
# name: preferred flavor (sour/sweet/fruity/milk/other),
#       liked ingredient group (api delivered/either ingredients with this word in name, or this word as its type),
#       disliked ingredient group (api delivered/either ingredients with this word in name, or this word as its type),
#       specific ingredient id that is extra liked
#       drink selection alcohol (hard-coded),
#       drink selection no alcohol (hard-coded)
#       heavy alcohol if alcohol true
npcDrinkPreferences = {"Santa": {"Flavor": "sweet",
                                 "Likes": "milk",
                                 "Dislikes": "fruit",
                                 "Favorite": "Mint",
                                 "alcohol" : a2,
                                 "no_alcohol": b2,
                                 "heavy_drinker": False},
                       "Cowboy": {"Flavor": "fruit",
                                  "Likes": "syrup",
                                   "Dislikes": "cream",
                                   "Favorite": "Milk",
                                   "alcohol" : a1,
                                   "no_alcohol": b1,
                                   "heavy_drinker": True},
                       "Pirate" : {"Flavor": "sour",
                                   "Likes": "fruit",
                                   "Dislikes": "coffee",
                                   "Favorite": "Coconut Milk",
                                   "alcohol" : a1,
                                   "no_alcohol": b1,
                                   "heavy_drinker": True}}

def initialize_supplies(username):
    supply_dict={}
    for item in get_all_ingredients():
        supply_dict[item] = 5
    # print(json.dumps(supply_dict))
    general_query("UPDATE players SET supplies=? WHERE username=?", [json.dumps(supply_dict), username])
    # print(select_query("SELECT * FROM players WHERE username=?", [username]))

def check_stock(username, added_ingredients):
    supply = json.loads(select_query("SELECT supplies FROM players WHERE username=?", [username])[0]["supplies"])
    for ingredient in added_ingredients:
        if supply[ingredient] < int(added_ingredients[ingredient]):
            return False
    return True

def change_stock(username, changes, mode):
    supply = json.loads(select_query("SELECT supplies FROM players WHERE username=?", [username])[0]["supplies"])
    for ingredient in changes:
        supply[ingredient] += mode * int(changes[ingredient])
    general_query("UPDATE players SET supplies=? WHERE username=?", [json.dumps(supply), username])


def get_npc_drink_preferences(name):
    return npcDrinkPreferences[name]

def npc_drink_order(name):
    drinkSet = []
    if alcoholOn:
        drinkSet = npcDrinkPreferences[name]["alcohol"] + npcDrinkPreferences[name]["no_alcohol"]
    else:
        drinkSet = npcDrinkPreferences[name]["no_alcohol"]


    if random.randint(1, 50) < 49:
        return drinkSet[random.randint(0, len(drinkSet) - 1)]
    else:
        return 0

def calculate_results(npc, drink, contents, usd):
    # print(usd)
    # print("\n\n")
    ingredients_used = contents.keys()
    ingredients_needed = drink["ingredients"]
    accuracy = len(ingredients_needed)
    npc_data = npcDrinkPreferences[npc]
    like = 5
    price = 0
    if len(ingredients_used) == 0:
        return (-5, 0)
    if (drink["drink"] != "Surprise Me!"):
        for ingredient in ingredients_needed:
            if not ingredient in ingredients_used:
                accuracy -= 1
        if accuracy < len(ingredients_needed)/2:
            if accuracy < len(ingredients_needed)/4:
                like = min(0, like - 2)
            like = min(0, like - 1)
    for ingredient in ingredients_used:
        amount = contents[ingredient]
        ingredient_info = ingredient_data[ingredient]
        if ingredient_info["flavor"] == "alcohol":
            if npc_data["heavy_drinker"]:
                like += amount - 1
            else:
                if contents[ingredient] > 1 or not ingredient in ingredients_needed:
                    like = min(0, like - 1)
        else:
            if npc_data["Likes"].lower() in ingredient or npc_data["Likes"].lower() == ingredient_info["flavor"].lower() or npc_data["Flavor"].lower() == ingredient_info["flavor"]:
                like += amount
            if npc_data["Favorite"].lower() == ingredient:
                like += 2 * amount
            elif npc_data["Dislikes"].lower() == ingredient_info["flavor"]:
                like = min(0, like - 1)
        price += ingredient_info["price"] * amount
    like -= 5
    result = "Good Drink!"
    if like == -5:
        result = "Terrible!"
    elif like < 0:
        result = "Could Be Better..."
    elif like > 0:
        "Wicked Drink!"
    elif like >= 5:
        result = "Perfection!"
    # result += " " + str(like)
    # print(usd["price_gram_10k"])
    money = round(price * float(usd)/10, 2)
    return (result, money, price)
    
def get_price(conversion_rate, item):
    price=ingredient_data[item]["price"]
    price *= conversion_rate / 10 * random.randint(90, 110) / 100
    return round(price, 2)

def get_qty():
    return random.randint(0,5)

def time_travel():
    day = random.randint(1, 28)
    month = random.randint(1,12)
    year = random.randint(0, 25)
    new_date = str(month) + "/" + str(day) + "/" + str(1999 + year)
    # print(date_to_timestamp(new_date))
    conversion_rate = request_value(date_to_timestamp(new_date))
    # print(conversion_rate)
    return (new_date, conversion_rate)

def timestamp_to_unix(date):
    temp = date.replace("/", "")
    year = int(temp[-4:])
    month = int(temp[:2])
    day = int(temp[2:4])
    time = 0
    time += (year - 1970) * 31556926
    time += (month) * 2629743
    time += day * 86400 
    return time

def request_coordinates(timestamp):
    unix_timestamp = timestamp_to_unix(timestamp)
    url = f"https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={unix_timestamp}"
    # timestamp is in unix/epoch time

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()[0]

        coordinates = [result["latitude"], result["longitude"]]

        return coordinates
    except requests.exceptions.RequestException as e:
        print(e)
        
# def request_country(coordinates):
#     url = f"https://api.wheretheiss.at/v1/coordinates/{coordinates[0]},{coordinates[1]}"
#     # use coordinates provided from request_coordinates()

#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#         result = response.json()

#         country = result["country_code"]
#         if country == "??":
#             country = "International Waters"
#         # default if ISS is above an ocean / international waters

#         return country
#     except requests.exceptions.RequestException as e:
#         print(e)


def request_value(timestamp):
    # print(timestamp)
    url = f"https://www.goldapi.io/api/XAU/USD/{timestamp}"
    # timestamp is in YYYYMMDD

    api_key = ""

    
    try:
        with open("keys/key_GoldAPI.txt", "r") as f:
            api_key = f.read().strip()
            # print(f.read().strip())
    except FileNotFoundError as e:
        print(e)
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        return(result)
    except requests.exceptions.RequestException as e:
        print(e)

def date_to_timestamp(date):
    temp = date.split("/")
    if int(temp[0]) < 10:
        temp[0] = "0" + temp[0]
    if int(temp[1]) < 10:
        temp[1] = "0" + temp[1] 
    out = temp[2] + temp[0] + temp[1]
    return int(out)