import requests
import gsheetstest as gs

SAMPLE_RANGE_NAME = 'prices!B2'  # Just store where the IATA Codes are
from flight_search import FlightSearch

class DataManager:
    def __init__(self):
        self.service = gs.authentic_sheets()
        self.city_list = gs.get_city_list(self.service)
        print(self.city_list)
        self.value_range_body = {
            "majorDimension": "COLUMNS",
            "values": [FlightSearch.iataassign(self.city_list)]
        }
        # Update IATA Codes in Google Sheet on init.
        self.update_response = gs.update_gsheets(self.service, SAMPLE_RANGE_NAME, "RAW", self.value_range_body)
