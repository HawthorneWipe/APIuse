# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)
from data_manager import DataManager
from flight_search import FlightSearch

# Create DataManager instance and initiate - fills the IATA Code column in google spreadsheet. Requires service email shared with Google Sheet
dm = DataManager()

flight_to_France = FlightSearch.kiwi_search(destination='CDG', price_max=1000)
# TODO That's a lot of data :) Grab date and e.g. convert local departure to datetime:
# datetime.datetime.fromisoformat(flight_to_France[0]['route'][0]['local_departure'][:19]).strftime('%X')
