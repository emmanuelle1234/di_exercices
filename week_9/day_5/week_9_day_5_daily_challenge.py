import datetime


class Airline:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.planes = []

    def __repr__(self):
        return f'Attributes of this airline\'s instance:\n'\
               f'- id: {self.id}\n'\
               f'- name: {self.name}\n'\
               f'- planes: {self.name}'

    def __str__(self):
        return f'Company: {self.name}'


class Airport:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.planes = []
        self.scheduled_departures = [] # The list of flights - Every future flight from this airport, sorted by date.
        self.scheduled_arrivals = [] # The list of flights - Every future flight to this airport, sorted by date.

    def __repr__(self):
        return f'Attributes of this airport\'s instance:\n'\
               f'- city: {self.city}\n'\
               f'- planes: {self.planes}\n'\
               f'- scheduled_departures: {self.scheduled_departures}\n'\
               f'- scheduled_arrivals: {self.scheduled_arrivals}'

    def __str__(self):
        return f'Airport of: {self.city}'

    def schedule_flight(self, destination, datetime):
        # Finds an available airplane from an airline, that serves the departure and the destination
        # Schedule the airplane for the flight
        pass

    def info(self, start_date, end_date):
        pass


class Airplane:
    def __init__(self, id: int, current_location: Airport, company: Airline):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []  # list of instances of class Flight sorted by datetime

    def __repr__(self):
        return f'Attributes of this airplane\'s instance:\n' \
               f'- id: {self.id}\n' \
               f'- current_location: {self.current_location}\n' \
               f'- company: {self.company}\n' \
               f'- next_flights: {self.next_flights}'

    def __str__(self):
        return f'An airplane from {self.company} is currently at {self.current_location}'

    def fly(self, destination):
        if not self.next_flights:
            print(f'This airplane is grounded for the time being.')
            return None
        elif self.next_flights[0].destination == destination:
            print(f'This airplane is going to take off')
            self.next_flights[0].take_off()
            print(f'This airplane is going to land')
            self.next_flights[0].land()
            self.next_flights.remove(self.next_flights[0])
            return destination
        elif destination in [self.next_flights[i].destination for i in range(len(self.next_flights))]:
            print(f'This airplane will fly to {destination} but later on. It\'s flying now to {self.next_flights[0].destination}.')
            return None
        else:
            print('Sorry but this destination is unknown in our Air Management System.')
            return None


    def location_on_date(self, date: datetime.date):
        # Returns where the plane will be on this date
        if not self.next_flights:
            print(f'This airplane is grounded for the time being.')
            return None
        elif date in [self.next_flights[i].date for i in range(len(self.next_flights))]:
            index = self.next_flights.index(date)
            location = self.next_flights[index].destination
            print(f'This airplane will be in {location} on {date}')
            return location
        else:
            print(f'This is not a correct input.')
            return None

    def available_on_date(self, date: datetime.date, location):
        # Returns True if the plane can fly from this location on this date
        # (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).
        for flight in self.next_flights:
            if location == self.location_on_date(date):
                return True
            else:
                return False
        pass


class Flight:
    def __init__(self, date: datetime.date, destination: Airport, origin: Airport, plane: Airplane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f'{self.destination}_{self.plane.company.id}_{self.date}'

    def __repr__(self):
        return f'Attributes of this flight\'s instance:\n' \
               f'- date: {self.date}\n' \
               f'- destination: {self.destination}\n' \
               f'- origin: {self.origin}\n' \
               f'- plane: {self.plane}'\
               f'- id: {self.id}\n'

    def __str__(self):
        return f' Departure: {self.date}\n'\
               f'From: {self.origin}\n'\
               f'To: {self.destination}\n' \
               f'Operated by: {self.plane.company}\n'

    def take_off(self):
        # self.plane has no more current location as origin
        pass

    def land(self):
        # self.plane current location becomes destination
        pass


# TESTING

cathay = Airline('CA', 'Cathay Pacific')
el_al = Airline('LY', 'El Al')
air_france = Airline('AF', 'Air France')
transavia = Airline('TR', 'Transavia')
american = Airline('AA', 'American Airlines')

cdg = Airport('CDG', 'Paris')
orly = Airport('ORY','Paris')
bg = Airport('BG','Tel Aviv')
jfk = Airport('JFK', 'New-York')
#air = Airport('InTheAir','SomeWhere')

plane1 = Airplane(21, cdg, el_al)
plane2 = Airplane(22, orly, el_al)
plane3 = Airplane(23, orly, transavia)
plane4 = Airplane(24, bg, el_al)
plane5 = Airplane(25, bg, air_france)
plane6 = Airplane(26, cdg, air_france)
plane7 = Airplane(27, jfk, american)
plane8 = Airplane(28, jfk, el_al)
plane9 = Airplane(29, jfk, air_france)
plane10 = Airplane(30, bg, american)
plane11 = Airplane(31, cdg, american)
plane12 = Airplane(32, bg, transavia)

flight1 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight2 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight3 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight4 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight5 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight6 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight7 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight8 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight9 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)
flight10 = Flight(datetime.date(2022, 5, 29), cdg, bg, plane6)

cathay.__repr__()
print(cathay)
print('\n')
plane5.fly(bg)
