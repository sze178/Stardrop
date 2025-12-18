# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

import requests

ingredient_data = {"Tia Maria" : {"flavor": "alcohol"},
                   "Vodka" : {"flavor": "alcohol"},
                   'Orange Juice' : {"flavor": "fruity"},
                   'Lemon Juice' : {"flavor": "sour"},
                   'Lime' : {"flavor": "sour"},
                   'Sugar' : {"flavor": "sweet"},
                   'Mint' : {"flavor": "other"},
                   'Jack Daniels' : {"flavor": "alcohol"},
                   'Melon Liqueur' : {"flavor": "fruit"},
                   'Sour Mix' : {"flavor": "sour"},
                   'Pineapple Juice' : {"flavor": "fruity"},
                   'Grenadine' : {"flavor": "sweet"},
                   'Sugar Syrup' : {"flavor": "sweet"},
                   'Angostura Bitters' : {"flavor": "other"},
                   'Rum' : {"flavor": "alcohol"},
                   'Grapefruit Juice' : {"flavor": "fruity"},
                   'Maraschino Liqueur' : {"flavor": "sweet"},
                   'Lime Juice' : {"flavor": "sour"},
                   'Brandy' : {"flavor": "alcohol"},
                   'Lemon' : {"flavor": "sour"},
                   'Powdered Sugar' : {"flavor": "sweet"},
                   'Cherry' : {"flavor": "fruity"},
                   'Sweet Vermouth' : {"flavor": "alcohol"},
                   'Bourbon' : {"flavor": "alcohol"},
                   'Ice' : {"flavor": "other"},
                   'Maraschino Cherry' : {"flavor": "sweet"},
                   'Orange Peel' : {"flavor": "fruity"},
                   'Coconut Milk' : {"flavor": "milky"},
                   'Pineapple' : {"flavor": "fruity"},
                   'Tequila' : {"flavor": "alcohol"},
                   'Gin' : {"flavor": "alcohol"},
                   'Coca-Cola' : {"flavor": "sweet"},
                   'Lemon Peel' : {"flavor": "sour"},
                   'Sherry' : {"flavor": "alcohol"},
                   'Orange Bitters': {"flavor": "other"},
                   'Lemonade' : {"flavor": "fruity"},
                   'Water' : {"flavor": "other"},
                   'Ginger' : {"flavor": "other"},
                   'Guava juice' : {"flavor": "fruity"},
                   'Peach Nectar' : {"flavor": "sweet"},
                   'Brown Sugar' : {"flavor": "sweet"},
                   'Cinnamon' : {"flavor": "other"},
                   'Cloves' : {"flavor": "other"},
                   'Passion Fruit Juice' : {"flavor": "fruity"},
                   'Ginger Ale' : {"flavor": "sweet"},
                   'Soda Water' : {"flavor": "other"},
                   'Mango' : {"flavor": "fruity"},
                   'Orange' : {"flavor": "fruity"},
                   'Apple Cider' : {"flavor": "fruity"},
                   'Allspice' : {"flavor": "other"},
                   'Nutmeg' : {"flavor": "other"},
                   'Light Cream' : {"flavor": "milky"},
                   'Egg White' : {"flavor": "milky"},
                   'Coffee Liqueur' : {"flavor": "milky"},
                   'Heavy Cream' : {"flavor": "milky"},
                   'Chocolate Liqueur' : {"flavor": "milky"},
                   'Amaretto' : {"flavor": "alcohol"},
                   'Chocolate Sauce' : {"flavor": "milky"},
                   'Salted Chocolate' : {"flavor": "sweet"},
                   'Scotch' : {"flavor": "alcohol"},
                   'Curacao' : {"flavor": "alcohol"},
                   'Half-and-Half' : {"flavor": "milky"},
                   'Condensed Milk' : {"flavor": "sweet"},
                   'Coconut Syrup' : {"flavor": "sweet"},
                   'Chocolate Syrup' : {"flavor": "milky"},
                   'Kahlua' : {"flavor": "alcohol"},
                   'Baileys Irish Cream' : {"flavor": "alcohol"},
                   'Vanilla Ice-Cream' : {"flavor": "milky"},
                   'Oreo cookie' : {"flavor": "sweet"},
                   'Coffee' : {"flavor": "milky"},
                   'Banana Liqueur' : {"flavor": "sweet"},
                   'Creme De Cacao' : {"flavor": "milky"},
                   'Chocolate Ice-Cream' : {"flavor": "milky"},
                   'Chocolate Milk' : {"flavor": "milky"},
                   'Whipped Cream' : {"flavor": "milky"},
                   'Banana' : {"flavor": "fruity"},
                   'Milk' : {"flavor": "milky"},
                   'Vanilla' : {"flavor": "sweet"},
                   'Chocolate' : {"flavor": "sweet"},
                   'Espresso' : {"flavor": "milky"},
                   'Egg Yolk' : {"flavor": "milky"}}

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

a1 = [58, 8603, 12212, 35427, 78945, 172502, 190753, 224615, 367321, 424489, 466077]
b1 = [43900, 357225, 499591, 627193, 778686, 805924]
a2 = [13554, 88538, 99612, 111282, 330969, 334642, 375884, 579225, 674837]
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

request_value(20251216)
