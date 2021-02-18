# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
from dotenv import load_dotenv, find_dotenv
import gsheetstest as gs
load_dotenv(find_dotenv(), verbose=True)
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

# Create DataManager instance and initiate - fills the IATA Code column in google spreadsheet. Requires service email shared with Google Sheet
DM = DataManager()
DM.updateIATA() # IATA codes to google sheet. Possibly update this for __init__ of DataManager to run on condition
# Create flights - returns array of flights that were found at a lower price than prices. Put prices and links in the google sheet
flights = FlightData.create_flights(DM.IATA_list, DM.prices)
for flight in flights:
    print(flight)
DM.updatePriceLinks(flights)

