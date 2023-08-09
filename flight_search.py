import requests

TEQUILA_API = "dHzz2X7SVOsKRRc_mTZdVOkDU9puYEbv"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, name: str):
        end_point = 'https://api.tequila.kiwi.com/locations/query'
        params = {
            "term": f"{name}",
            "locale": "en-US"
        }
        headers = {
            "accept": "application/json",
            "apikey": TEQUILA_API
        }

        response = requests.get(url=end_point, params=params, headers=headers)
        iata_code = response.json()["locations"][0]['code']
        return iata_code
