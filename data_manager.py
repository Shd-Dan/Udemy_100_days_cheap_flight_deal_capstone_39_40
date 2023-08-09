import requests
from pprint import pprint

END_POINT = "https://api.sheety.co/4f36951749eb4b5bf9f4ed2b117df48b/udemyFlightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.information_data = {}

    def get_data(self):
        respond = requests.get(url=END_POINT)
        self.information_data = respond.json()["prices"]
        return self.information_data

    def update_iata_code(self, code: str, city_id: int):
        params = {
            "price": {
                'iataCode': f"{code}"
            }
        }
        response = requests.put(url=f"{END_POINT}/{city_id}", json=params)
        print(response.text)
