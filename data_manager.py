import requests
from flight_search import FlightSearch
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account


class DataManager:
    RANGE_NAME_IATA = 'prices!B2'  # Just store where the IATA Codes are
    RANGE_NAME_PRICE_LINK = 'prices!D2'

    def __init__(self):
        self.service = self.authentic_sheets()
        self.prices = self.get_prices_list(self.service)
        self.city_list = self.get_city_list(self.service)
        self.IATA_list = FlightSearch.iataassign(self.city_list)
        self.value_range_body_city_list_IATA = {
            "majorDimension": "COLUMNS",
            "values": [self.IATA_list]
        }

    def authentic_sheets(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'credentials.json'
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        return service

    def updateIATA(self):
        # print(self.value_range_body_city_list_IATA)
        self.update_gsheets(self.service,
                            DataManager.RANGE_NAME_IATA,
                            "RAW",
                            self.value_range_body_city_list_IATA)

    def updatePriceLinks(self, flights):
        self.update_gsheets(self.service,
                            DataManager.RANGE_NAME_PRICE_LINK,
                            "RAW",
                            value_range_body={
                                "majorDimension": "ROWS",
                                "values": [
                                    [flight.price, flight.link] if flight is not None else ['Not Found', 'Not Found']
                                    for flight in flights]
                            })

    def update_gsheets(self, service, sheetrange, value_input_option, value_range_body):
        response = service.spreadsheets().values().update(spreadsheetId=os.getenv('SPREADSHEET_ID'),
                                                          range=sheetrange,
                                                          valueInputOption=value_input_option,
                                                          body=value_range_body).execute()


    def get_city_list(self, service):
        range_city = 'prices!A2:A'
        request = service.spreadsheets().values().get(spreadsheetId=os.getenv('SPREADSHEET_ID'),
                                                      range=range_city).execute()
        val = request.get('values', [])  # return empty if no values
        return val

    def get_prices_list(self, service):
        range_city = 'prices!C2:C'
        request = service.spreadsheets().values().get(spreadsheetId=os.getenv('SPREADSHEET_ID'),
                                                      range=range_city, valueRenderOption="UNFORMATTED_VALUE").execute()
        val = request.get('values', [])  # return empty if no values
        return val
