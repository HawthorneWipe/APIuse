import requests
import json
import os


class FlightSearch:
    def __init__(self):
        pass

    @staticmethod
    def iataassign(city):
        iata = []
        kiwi_endpoint = os.getenv('kiwi_endpoint')
        for cit in city:
            params_kiwi = {
                'term': cit,
                'location_types': 'airport',
                'active_only': 'true',
                'limit': 1
            }
            headers_kiwi = {
                'apikey': os.getenv('KIWI_API_KEY'),
                'Content-Type': 'application/json',
            }

            reskiwi = requests.get(url=f"{kiwi_endpoint}query", params=params_kiwi, headers=headers_kiwi)
            iata.append(reskiwi.json()['locations'][0]['code'])
        return iata
