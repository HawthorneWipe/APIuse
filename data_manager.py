import requests
import gsheetstest as gs
from flight_search import FlightSearch


class DataManager:
    RANGE_NAME_IATA = 'prices!B2'  # Just store where the IATA Codes are

    def __init__(self):
        self.service = gs.authentic_sheets()
        self.prices = gs.get_prices_list(self.service)
        self.city_list = gs.get_city_list(self.service)
        self.IATA_list = FlightSearch.iataassign(self.city_list)
        self.value_range_body_city_list_IATA = {
            "majorDimension": "COLUMNS",
            "values": [self.IATA_list]
        }
        # Update IATA Codes in Google Sheet on init.
        self.update_response = gs.update_gsheets(self.service,
                                                 DataManager.RANGE_NAME_IATA,
                                                 "RAW",
                                                 self.value_range_body_city_list_IATA)
