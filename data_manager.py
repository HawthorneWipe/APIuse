import requests
import gsheetstest as gs
from flight_search import FlightSearch


class DataManager:
    RANGE_NAME_IATA = 'prices!B2'  # Just store where the IATA Codes are
    RANGE_NAME_PRICE_LINK = 'prices!D2'

    def __init__(self):
        self.service = gs.authentic_sheets()
        self.prices = gs.get_prices_list(self.service)
        self.city_list = gs.get_city_list(self.service)
        self.IATA_list = FlightSearch.iataassign(self.city_list)
        self.value_range_body_city_list_IATA = {
            "majorDimension": "COLUMNS",
            "values": [self.IATA_list]
        }

    def updateIATA(self):
        # print(self.value_range_body_city_list_IATA)
        gs.update_gsheets(self.service,
                          DataManager.RANGE_NAME_IATA,
                          "RAW",
                          self.value_range_body_city_list_IATA)

    def updatePriceLinks(self, flights):
        gs.update_gsheets(self.service,
                          DataManager.RANGE_NAME_PRICE_LINK,
                          "RAW",
                          value_range_body={
                              "majorDimension": "ROWS",
                              "values": [[flight.price, flight.link] if flight is not None else ['Not Found', 'Not Found']
                                         for flight in flights]
                          })

    def update_gsheets(self, service, sheetrange, value_input_option, value_range_body):
        response = service.spreadsheets().values().update(spreadsheetId=os.getenv('SPREADSHEET_ID'),
                                                          range=sheetrange,
                                                          valueInputOption=value_input_option,
                                                          body=value_range_body).execute()
        print(response)
