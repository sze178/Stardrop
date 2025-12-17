from recipes import *
from game_state import *

ingredients = {}
for drink in a1:
    for ingredient in request_drink(drink)["ingredients"]:
        if not ingredient in ingredients:
            ingredients[ingredient] = "0"
for drink in b1:
    for ingredient in request_drink(drink)["ingredients"]:
        if not ingredient in ingredients:
            ingredients[ingredient] = "0"
for drink in a2:
    for ingredient in request_drink(drink)["ingredients"]:
        if not ingredient in ingredients:
            ingredients[ingredient] = "0"
for drink in b2:
    for ingredient in request_drink(drink)["ingredients"]:
        if not ingredient in ingredients:
            ingredients[ingredient] = "0"

print(ingredients.keys())
