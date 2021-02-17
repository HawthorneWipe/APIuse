import requests
import datetime
import os


class FlightSearch:
    FLY_FROM = os.getenv('FLY_FROM')
    kiwi_api_key = os.getenv('KIWI_API_KEY')
    kiwi_endpoint = os.getenv('kiwi_endpoint')
    kiwi_endpoint_search = os.getenv('kiwi_endpoint_search')
    kiwi_endpoint_search_multi = os.getenv('kiwi_endpoint_search_multi')
    headers_kiwi = {
        "apikey": kiwi_api_key,
        'Content-Type': 'application/json',
        'Content-Encoding': 'gzip'
    }
    def __init__(self):
        pass

    @classmethod
    def kiwi_search(cls, destination, price_max):
        # code parameters here, no need for that many arguments.
        params_kiwi = {
            'fly_from': cls.FLY_FROM,
            'fly_to': destination,
            'date_from': (datetime.date.today() + datetime.timedelta(1)).strftime('%d/%m/%Y'),
            'date_to': (datetime.date.today() + datetime.timedelta(180)).strftime('%d/%m/%Y'),
            'nights_in_dst_from': 2,
            'nights_in_dst_to': 7,
            'flight_type': 'round',
            'curr': 'GBP',
            'price_to': price_max,
            'max_stopovers': 0
            }
        reskiwi = requests.get(url=f"{cls.kiwi_endpoint_search}", params=params_kiwi, headers=cls.headers_kiwi)
        reskiwi.raise_for_status()
        #Get only the first entry. Can change later if needed. No permission for multi_search.
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
            reskiwi = requests.get(url=f"{cls.kiwi_endpoint}query", params=params_kiwi, headers=cls.headers_kiwi)
            iata.append(reskiwi.json()['locations'][0]['code'])
        return iata
