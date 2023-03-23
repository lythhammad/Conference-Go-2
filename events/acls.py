import requests
import json
from .keys import PEXEL_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    headers = {"Authorization": f"{PEXEL_KEY}"}
    url = f"https://api.pexels.com/v1/search?query={city}+{state}"

    response = requests.get(url, headers=headers)

    data = response.json()
    return data["photos"][0]["src"]["original"]


# def get_wether_data(city, state):
