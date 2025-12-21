# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

from recipes import *
from db import *
import random, json

alcoholOn = True
npc_at_seat = ["Santa"]

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
                       "Cowboy": {"Flavor": "fruity",
                                  "Likes": "syrup",
                                   "Dislikes": "cream",
                                   "Favorite": 225156,
                                   "alcohol" : a1,
                                   "no_alcohol": b1,
                                   "heavy_drinker": True},
                       "Agent J": {"Flavor": "milky",
                                   "Likes": "chocolate",
                                   "Dislikes": "soda",
                                   "Favorite": 0,
                                   "alcohol" : a2,
                                   "no_alcohol": b2,
                                   "heavy_drinker": False},
                       "Pirate" : {"Flavor": "sour",
                                   "Likes": "fruit",
                                   "Dislikes": "coffee",
                                   "Favorite": 0,
                                   "alcohol" : a1,
                                   "no_alcohol": b1,
                                   "heavy_drinker": True}}

def initialize_supplies(username):
    supply_dict={}
    for item in get_all_ingredients():
        supply_dict[item] = 0
    # print(json.dumps(supply_dict))
    general_query("UPDATE players SET supplies=? WHERE username=?", [json.dumps(supply_dict), username])
    # print(select_query("SELECT * FROM players WHERE username=?", [username]))

def get_npc_drink_preferences(name):
    return npcDrinkPreferences[name]

def set_last_order(drink, npc):
    last_drink_order = drink
    last_npc = npc
    print(last_drink_order)

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

def calculate_results(npc, drink, contents):
    pass
    ingredients_used = contents.keys()
    ingredients_needed = drink["ingredients"]
    accuracy = len(ingredients_needed)
    npc_data = npcDrinkPreferences[npc]
    # ingredient_info = ingredient_data[ingredient]
    like = 5
    price = 0
    # for ingredient in ingredients_needed:
    #     if not ingredient in ingredients_used:
    #         accuracy -= 1
    # if accuracy < len(ingredients_needed)/2:
    #     like -= 1
    # for ingredient in ingredients_used:
    #     if npc_data["Likes"] in ingredient or npc_data["Likes"] == ingredient_info["flavor"]:
    #         like += 1
    #     if npc_data["Favorite"] == ingredient:
    #         like += 2
    #     elif npc_data["Dislikes"] == ingredient_info["flavor"]:
    #         like -= 1
    #     price += ingredient_info["price"]
    return (like, price)
    
def request_coordinates(timestamp):
    url = f"https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={timestamp}"
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
    url = f"https://www.goldapi.io/api/XAU/USD/{timestamp}"
    # timestamp is in YYYYMMDD

    api_key = ""

    '''
    try:
        with open("keys/key_GoldAPI.txt", "r") as f:
            api_key = f.read().strip()
            print(f.read().strip())
    except FileNotFoundError as e:
        print(e)
    '''

    api_key = "goldapi-citmsmixc4q0y-io" #read key_GoldAPI.txt later
    print(api_key)
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.text
        print(result)
    except requests.exceptions.RequestException as e:
        print(e)

def date_to_timestamp(date):
    temp = date.replace("/", "")
    temp = temp[-4:] + temp[:2] + temp[2:4]
    return int(temp)