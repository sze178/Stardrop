# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

from recipes import *
from db import *
import random, json

alcoholOn = True
npc_at_seat = ["Santa"]

last_drink_order = {}
last_npc = ""

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

def calculate_results(made):
    pass
    ingredients_used = made.keys()
    ingredients_needed = last_drink_order["ingredients"]
    accuracy = len(ingredients_needed)
    npc_data = npcDrinkPreferences[last_npc]
    ingredient_info = ingredient_data[ingredient]
    like = 5
    price = 0
    for ingredient in ingredients_needed:
        if not ingredient in ingredients_used:
            accuracy -= 1
    if accuracy < len(ingredients_needed)/2:
        like -= 1
    for ingredient in ingredients_used:
        if npc_data["Likes"] in ingredient or npc_data["Likes"] == ingredient_info["flavor"]:
            like += 1
        if npc_data["Favorite"] == ingredient:
            like += 2
        elif npc_data["Dislikes"] == ingredient_info["flavor"]:
            like -= 1
        price += ingredient_info["price"]
    return (like, price)
    

        
    