import requests

def request_ingredients(id):
    url = f"https://boozeapi.com/api/v1/cocktails/{id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        result = response.json()
        ingredients = result["ingredients"]
        print(result["name"] + ":")
        for ingredient in ingredients:
            print(ingredient["name"])
    except requests.exceptions.RequestException as e:
        print(e)

request_ingredients(58)
print("---------------")
request_ingredients(809)
