# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

import requests

ingredient_data = {"Tia Maria" : {"flavor": "alcohol", "price": 4},
                   "Vodka" : {"flavor": "alcohol", "price": 4},
                   'Orange Juice' : {"flavor": "fruity", "price": 2},
                   'Lemon Juice' : {"flavor": "sour", "price": 2},
                   'Lime' : {"flavor": "sour", "price": 3},
                   'Sugar' : {"flavor": "sweet", "price": 1},
                   'Mint' : {"flavor": "other", "price": 1},
                   'Jack Daniels' : {"flavor": "alcohol", "price": 4},
                   'Melon Liqueur' : {"flavor": "fruit", "price": 2},
                   'Sour Mix' : {"flavor": "sour", "price": 1},
                   'Pineapple Juice' : {"flavor": "fruity", "price": 2},
                   'Grenadine' : {"flavor": "sweet", "price": 1},
                   'Sugar Syrup' : {"flavor": "sweet", "price": 1},
                   'Angostura Bitters' : {"flavor": "other", "price": 1},
                   'Rum' : {"flavor": "alcohol", "price": 4},
                   'Grapefruit Juice' : {"flavor": "fruity", "price": 2},
                   'Maraschino Liqueur' : {"flavor": "sweet", "price": 1},
                   'Lime Juice' : {"flavor": "sour", "price": 2},
                   'Brandy' : {"flavor": "alcohol", "price": 4},
                   'Lemon' : {"flavor": "sour", "price": 3},
                   'Powdered Sugar' : {"flavor": "sweet", "price": 1},
                   'Cherry' : {"flavor": "fruity", "price": 3},
                   'Sweet Vermouth' : {"flavor": "alcohol", "price": 4},
                   'Bourbon' : {"flavor": "alcohol", "price": 4},
                   'Ice' : {"flavor": "other", "price": 1},
                   'Maraschino Cherry' : {"flavor": "sweet", "price": 1},
                   'Orange Peel' : {"flavor": "fruity", "price": 1},
                   'Coconut Milk' : {"flavor": "milky", "price": 2},
                   'Pineapple' : {"flavor": "fruity", "price": 3},
                   'Tequila' : {"flavor": "alcohol", "price": 4},
                   'Gin' : {"flavor": "alcohol", "price": 4},
                   'Coca-Cola' : {"flavor": "sweet", "price": 2},
                   'Lemon Peel' : {"flavor": "sour", "price": 1},
                   'Sherry' : {"flavor": "alcohol", "price": 4},
                   'Orange Bitters': {"flavor": "other", "price": 1},
                   'Lemonade' : {"flavor": "fruity", "price": 3},
                   'Water' : {"flavor": "other", "price": 1},
                   'Ginger' : {"flavor": "other", "price": 3},
                   'Guava juice' : {"flavor": "fruity", "price": 2},
                   'Peach Nectar' : {"flavor": "sweet", "price": 2},
                   'Brown Sugar' : {"flavor": "sweet", "price": 1},
                   'Cinnamon' : {"flavor": "other", "price": 1},
                   'Cloves' : {"flavor": "other", "price": 1},
                   'Passion Fruit Juice' : {"flavor": "fruity", "price": 2},
                   'Ginger Ale' : {"flavor": "sweet", "price": 2},
                   'Soda Water' : {"flavor": "other", "price": 2},
                   'Mango' : {"flavor": "fruity", "price": 3},
                   'Orange' : {"flavor": "fruity", "price": 3},
                   'Apple Cider' : {"flavor": "fruity", "price": 2},
                   'Allspice' : {"flavor": "other", "price": 1},
                   'Nutmeg' : {"flavor": "other", "price": 1},
                   'Light Cream' : {"flavor": "milky", "price": 1},
                   'Egg White' : {"flavor": "milky", "price": 3},
                   'Coffee Liqueur' : {"flavor": "milky", "price": 2},
                   'Heavy Cream' : {"flavor": "milky", "price": 1},
                   'Chocolate Liqueur' : {"flavor": "milky", "price": 2},
                   'Amaretto' : {"flavor": "alcohol", "price": 4},
                   'Chocolate Sauce' : {"flavor": "milky", "price": 1},
                   'Salted Chocolate' : {"flavor": "sweet", "price": 1},
                   'Scotch' : {"flavor": "alcohol", "price": 4},
                   'Curacao' : {"flavor": "alcohol", "price": 4},
                   'Half-and-Half' : {"flavor": "milky", "price": 1},
                   'Condensed Milk' : {"flavor": "sweet", "price": 1},
                   'Coconut Syrup' : {"flavor": "sweet", "price": 1},
                   'Chocolate Syrup' : {"flavor": "milky", "price": 1},
                   'Kahlua' : {"flavor": "alcohol", "price": 4},
                   'Baileys Irish Cream' : {"flavor": "alcohol", "price": 4},
                   'Vanilla Ice-Cream' : {"flavor": "milky", "price": 2},
                   'Oreo cookie' : {"flavor": "sweet", "price": 2},
                   'Coffee' : {"flavor": "milky", "price": 2},
                   'Banana Liqueur' : {"flavor": "sweet", "price": 1},
                   'Creme De Cacao' : {"flavor": "milky", "price": 2},
                   'Chocolate Ice-Cream' : {"flavor": "milky", "price": 2},
                   'Chocolate Milk' : {"flavor": "milky", "price": 2},
                   'Whipped Cream' : {"flavor": "milky", "price": 1},
                   'Banana' : {"flavor": "fruity", "price": 3},
                   'Milk' : {"flavor": "milky", "price": 2},
                   'Vanilla' : {"flavor": "sweet", "price": 2},
                   'Chocolate' : {"flavor": "sweet", "price": 2},
                   'Espresso' : {"flavor": "milky", "price": 2},
                   'Egg Yolk' : {"flavor": "milky", "price": 3},
                   	"Sambuca" : {"flavor": "alcohol", "price": 4},
                    "Blackberries" : {"flavor": "fruity", "price": 3}}

ingredient_fixes = {"Añejo Rum": "Rum",
                    "Light Rum": "Rum",
                    "Dark Rum": "Rum",
                    'Midori Melon Liqueur': "Melon Liqueur",
                    "lemon": "Lemon",
                    'Dark Creme De Cacao': "Creme De Cacao",
                    'Half-and-half': "Half-and-Half",
                    'Passion fruit juice': "Passion Fruit Juice",
                    'Heavy cream': "Heavy Cream",
                    'Chocolate Ice-cream': "Chocolate Ice-Cream"
                    }
def get_all_ingredients():
    return ingredient_data.keys()

def request_drink(id):
    if id == 0:
        return {"drink": "ANYTHING", "ingredients": ["Egg White"]}

    url = f"https://boozeapi.com/api/v1/cocktails/{id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()
        ingredients = []
        for i in result["ingredients"]:
            if i["name"] in ingredient_fixes:
                ingredients.append(ingredient_fixes[i["name"]])
            elif i["name"] in ingredient_data:
                ingredients.append(i["name"])
        drink_data = {"drink": result["name"],
                      "ingredients": ingredients}

        return drink_data
    except requests.exceptions.RequestException as e:
        print(e)

a1 = [58, 8603, 12212, 35427, 78945, 172502, 190753, 224615, 367321, 424489, 466077, 707958, 722986, 754242, 762423]
b1 = [43900, 357225, 499591, 627193, 778686, 805924]
a2 = [13554, 88538, 99612, 111282, 330969, 334642, 375884, 579225, 674837, 722986, 728941, 737623]
b2 = [42501, 264361, 434283, 577385, 934558]


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

def request_country(coordinates):
    url = f"https://api.wheretheiss.at/v1/coordinates/{coordinates[0]},{coordinates[1]}"
    # use coordinates provided from request_coordinates()

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()

        country = result["country_code"]
        if country == "??":
            country = "International Waters"
        # default if ISS is above an ocean / international waters

        return country
    except requests.exceptions.RequestException as e:
        print(e)


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

# request_value(20251216)
