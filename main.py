# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()
for city in sheet_data:
    city_name = city["city"]
    id_city = city["id"]
    iata_code = flight_search.get_iata_code(city_name)
    city['iataCode'] = data_manager.update_iata_code(iata_code, id_city)


