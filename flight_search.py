import requests
import datetime
import os
kiwi_endpoint = os.getenv('kiwi_endpoint')
kiwi_endpoint_search = os.getenv('kiwi_endpoint_search')
kiwi_api_key = os.getenv('KIWI_API_KEY')
#For now, hardcode the departure place
FLY_FROM = "GLA"

class FlightSearch:
    def __init__(self):
        pass
    @classmethod
    def kiwi_search(cls, destination, price_max):
        params_kiwi = {
            'fly_from': FLY_FROM,
            'fly_to': destination,
            'date_from': (datetime.date.today()+datetime.timedelta(1)).strftime('%d/%m/%Y'),
            'date_to': (datetime.date.today()+datetime.timedelta(180)).strftime('%d/%m/%Y'),
            'nights_in_dst_from': 2,
            'nights_in_dst_to': 7,
            'flight_type': 'round',
            'curr': 'GBP',
            'price_to': price_max,
            'max_stopovers': 0
        }
        headers_kiwi = {
            'apikey': kiwi_api_key,
            'Content-Type': 'application/json',
        }
        reskiwi = requests.get(url=f"{kiwi_endpoint_search}", params=params_kiwi, headers=headers_kiwi)
        print(reskiwi.json())
        return reskiwi.json()['data']
    # Search IATA Code for cities in city list. Returns list of iata codes for cities in city list.
    @classmethod
    def iataassign(cls, city):
        iata = []
        for cit in city:
            params_kiwi = {
                'term': cit,
                'location_types': 'airport',
                'active_only': 'true',
                'limit': 1
            }
            headers_kiwi = {
                'apikey': kiwi_api_key,
                'Content-Type': 'application/json',
            }

            reskiwi = requests.get(url=f"{kiwi_endpoint}query", params=params_kiwi, headers=headers_kiwi)
            iata.append(reskiwi.json()['locations'][0]['code'])
        return iata
