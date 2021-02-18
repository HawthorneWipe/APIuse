from flight_search import FlightSearch
import gsheetstest as gs

class FlightData():
    # This class is responsible for structuring the flight data.
    def __init__(self, price, destination_city_code, date_of_flight, date_of_return, link):
        self.price = price
        self.destination_city_code = destination_city_code
        self.date_of_flight = date_of_flight
        self.date_of_return = date_of_return
        self.link = link
        print(self)

    def __str__(self):
        return f'Flight created: flight to {self.destination_city_code} on {self.date_of_flight} to {self.date_of_return} costing {self.price}'

    @classmethod
    def create_flights(cls, IATA_list, prices):
        # kiwi response is a dit: dict_keys(['id', 'nightsInDest', 'duration', 'flyFrom', 'cityFrom', 'cityCodeFrom',
        # 'countryFrom', 'flyTo', 'cityTo', 'cityCodeTo', 'countryTo', 'distance', 'routes', 'airlines', 'pnr_count',
        # 'has_airport_change', 'technical_stops', 'price', 'bags_price', 'baglimit', 'availability',
        # 'facilitated_booking_available', 'conversion', 'quality', 'booking_token', 'deep_link', 'tracking_pixel',
        # 'transfers', 'type_flights', 'virtual_interlining', 'route', 'local_arrival', 'utc_arrival', 'local_departure',
        # 'utc_departure'])
        flights = []
        for city, price in zip(IATA_list, prices):
            FoundFlight = FlightSearch.kiwi_search(city, price)
            if not FoundFlight:
                flights.append(None)
                print(f"No flights to {city} at the set price")
            else:
                flights.append(cls(FoundFlight[0]['price'], FoundFlight[0]['cityTo'],
                                              FoundFlight[0]['route'][0]['local_departure'],
                                              FoundFlight[0]['route'][1]['local_departure'], FoundFlight[0]['deep_link']))
        return flights
