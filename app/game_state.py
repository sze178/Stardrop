
import random

alcoholOn = True

#drink selections / list of ids from api to randomly choose from
#a if alcohol b if not
a1 = ["test1", "test2", "test3", "test4"]
b1 = []
a2 = []
b2 = []
#npcDrinkPreferences: 
# name: preferred flavor (sour/sweet/fruity/milky), 
#       liked ingredient group (api delivered/either ingredients with this word in name, or this word as its type), 
#       disliked ingredient group (api delivered/either ingredients with this word in name, or this word as its type),
#       specific ingredient id that is extra liked
#       drink selection alcohol (hard-coded),
#       drink selection no alcohol (hard-coded)  
#       heavy alcohol if alcohol true
npcDrinkPreferences = {"santa": {"flavor": "sweet",
                                 "likes": "mint",
                                 "dislikes": "fruit",
                                 "favorite": 402412,
                                 "alcohol" : a1,
                                 "no_alcohol": b1,
                                 "heavy_drinker": False},
                       "cowboy": {"flavor": "milky",
                                 "likes": "cream",
                                 "dislikes": "syrup",
                                 "favorite": 225156,
                                 "alcohol" : a1,
                                 "no_alcohol": b1,
                                 "heavy_drinker": True}}



def get_npc_drink_preferences(name):
    return npcDrinkPreferences[name]

def npc_drink_order(name):
    drinkSet = []
    if alcoholOn:
        drinkSet = npcDrinkPreferences[name][4]
    else:
        drinkSet = npcDrinkPreferences[name][5]
    
    return drinkSet[random.randint(0, len(drinkSet) - 1)]
