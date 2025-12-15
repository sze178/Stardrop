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
