import requests

ingredient_data = {"Añejo Rum": 0}

#['Añejo Rum', 'Tia Maria', 'Vodka', 'Orange Juice', 'Lemon Juice', 'Light Rum', 'Lime', 'Sugar', 'Mint', 'Jack Daniels', 'Midori Melon Liqueur', 'Sour Mix', 'Dark Rum', 'Pineapple Juice', 'Grenadine', 'Sugar Syrup', 'Angostura Bitters', 'Rum', 'Grapefruit Juice', 'Maraschino Liqueur', 'Lime Juice', 'Brandy', 'lemon', 'Powdered Sugar', 'Cherry', 'Sweet Vermouth', 'Bourbon', 'Ice', 'Maraschino Cherry', 'Orange Peel', 'Coconut Milk', 'Pineapple', 'Tequila', 'Gin', 'Coca-Cola', 'Lemon Peel', 'Sherry', 'Orange Bitters', 'Lemonade', 'Water', 'Ginger', 'Guava juice', 'Peach Nectar', 'Brown Sugar', 'Cinnamon', 'Cloves', 'Passion fruit juice', 'Ginger Ale', 'Soda Water', 'Mango', 'Orange', 'Apple Cider', 'Allspice', 'Nutmeg', 'Light Cream', 'Egg White', 'Coffee Liqueur', 'Heavy cream', 'Chocolate Liqueur', 'Amaretto', 'Chocolate Sauce', 'Salted Chocolate', 'Scotch', 'Curacao', 'Half-and-half', 'Condensed Milk', 'Coconut Syrup', 'Chocolate Syrup', 'Kahlua', 'Baileys Irish Cream', 'Vanilla Ice-Cream', 'Oreo cookie', 'Dark Creme De Cacao', 'Coffee', 'Banana Liqueur', 'Creme De Cacao', 'Chocolate Ice-cream', 'Chocolate Milk', 'Whipped Cream', 'Banana', 'Milk', 'Vanilla', 'Chocolate', 'Espresso', 'Egg Yolk']


def request_drink(id):
    if id == 0:
        return {"drink": "ANYTHING", "ingredients": ["uranium"]}

    url = f"https://boozeapi.com/api/v1/cocktails/{id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()
        ingredients = []
        for i in result["ingredients"]:
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


def request_position(timestamp):
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


def request_value(timestamp):
    url = f"https://www.goldapi.io/api/XAU/USD/{timestamp}"
    # timestamp is in YYYYMMDD

    api_key = ""

    '''
    try:
        with open("keys/key_GoldAPI.txt", "r") as f:
            api_key = f.read().strip()
    except FileNotFoundError:
        print("GoldAPI key not found")
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
