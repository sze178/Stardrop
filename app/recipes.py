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

