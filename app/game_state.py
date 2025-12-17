
import random

alcoholOn = True
npc_at_seat = ["santa"]

#drink selections / list of ids from api to randomly choose from
#a if alcohol b if not
#1 fruity/sour
#2 milky/sweet
a1 = [58, 8603, 12212, 35427, 78945, 172502, 190753, 224615, 367321, 424489, 466077]
b1 = [43900, 357225, 499591, 627193, 778686, 805924]
a2 = [13554, 88538, 99612, 111282, 330969, 334642, 375884, 579225, 674837]
b2 = [42501, 264361, 434283, 577385, 934558]
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
                                 "alcohol" : a2,
                                 "no_alcohol": b2,
                                 "heavy_drinker": False},
                       "cowboy": {"flavor": "fruity",
                                  "likes": "syrup",
                                   "dislikes": "cream",
                                   "favorite": 225156,
                                   "alcohol" : a1,
                                   "no_alcohol": b1,
                                   "heavy_drinker": True},
                       "agent j": {"flavor": "milky",
                                   "likes": "chocolate",
                                   "dislikes": "soda",
                                   "favorite": 0,
                                   "alcohol" : a2,
                                   "no_alcohol": b2,
                                   "heavy_drinker": False},
                       "pirate" : {"flavor": "sour",
                                   "likes": "fruit",
                                   "dislikes": "coffee",
                                   "favorite": 0,
                                   "alcohol" : a1,
                                   "no_alcohol": b1,
                                   "heavy_drinker": True}}



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
