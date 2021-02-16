#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), verbose=True)
from data_manager import DataManager
from flight_search import FlightSearch

#Create DataManager instance and initiate - fills the IATA Code column in google spreadsheet. It will ask for authentication from Google
dm = DataManager()
