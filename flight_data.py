import os
from flight_search import FlightSearch
KIWI_API_KEY = os.getenv('KIWI_API_KEY')

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price: int
        self.destination_city_code: str
        self.price_max: int
        self.response = FlightSearch.kiwi_search(destination='CDG', price_max=1000)

