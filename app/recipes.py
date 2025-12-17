import requests

ingredient_data = {}

def request_drink(id):
    url = f"https://boozeapi.com/api/v1/cocktails/{id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()

        drink_data = {result["name"]: result["ingredients"]}

        return drink_data
    except requests.exceptions.RequestException as e:
        print(e)

a1 = [58, 8603, 12212, 35427, 78945, 172502, 190753, 224615, 367321, 424489, 466077]
b1 = [43900, 357225, 499591, 627193, 778686, 805924]
a2 = [13554, 88538, 99612, 111282, 330969, 334642, 375884, 579225, 674837]
b2 = [42501, 264361, 434283, 577385, 934558]

def process_drink_response(drink_resp: dict, ingredient_data: dict):
    # drink_resp looks like: { "Drink Name": [ { "id": ..., "name": ... }, ... ] }
    for _drink_name, ingredients in (drink_resp or {}).items():
        for ing in ingredients or []:
            ing_name = ing.get("name")
            ing_id = ing.get("id")
            if ing_name and ing_id is not None and ing_name not in ingredient_data:
                ingredient_data[ing_name] = ing_id

all_drink_ids = []
for ids in (a1, b1, a2, b2):
    all_drink_ids.extend(ids)

for drink_id in all_drink_ids:
    drink_resp = request_drink(drink_id)   # your function that returns the dict shown in your example
    process_drink_response(drink_resp, ingredient_data)

print(ingredient_data)

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

    api_key = "goldapi-citmsmixc4q0y-io" #read key_GoldAPI.txt later

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

request_value(20251214)
