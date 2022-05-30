# EXERCISE 1 :
import statistics


class Building:

    buildings_list = []

    def __init__(self, address: str):
        self.address = address
        self.inhabitants = [] # why we need two inhabitants lists?
        self.buildings_list.append([self.address])
        self.inhabitants_list = []

    def inhabitants_name(self):
        for i in self.inhabitants:
            if i.name not in self.inhabitants_list:
                self.inhabitants_list.append(i.name)
        return self.inhabitants_list

    def __str__(self):
        return self.address


class Human:
    def __init__(self, name: str, age: int, living_place='None'):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building: Building):
        if self not in building.inhabitants:
            self.living_place = building
            building.inhabitants.append(self)
            print(building.inhabitants)

    def __str__(self):
        return f'{self.name} lives at {self.living_place}'


class City:
    def __init__(self, name, buildings=[]):
        self.name = name
        self.buildings = buildings
        self.buildings_addresses = []

    def construct(self, address):
        self.buildings.append(Building(address))

    def buildings_addr(self):
        for i in self.buildings:
            if i.address not in self.buildings_addresses:
                self.buildings_addresses.append(i.address)
        return self.buildings_addresses

    def info(self): # not understood why address was proposed (I made the assumption of a bijection building/address)
        buildings_number = len(self.buildings)
        counter = 0
        for building in self.buildings:
            counter += len(building.inhabitants) # problem with inhabitants list
        return f'Number of buildings in {self.name}: {buildings_number}\nMean age of citizens in buildings: {counter/buildings_number}'


# TESTING

human1 = Human('human1', 12)
human2 = Human('human2', 75)
human3 = Human('human3', 27)
human4 = Human('human4', 49)
human5 = Human('human5', 31)
human6 = Human('human6', 3)
human7 = Human('human7', 36)
human8 = Human('human8', 25)
human9 = Human('human9', 26)
human10 = Human('human10', 50)

buildingA = Building('rehov HaTikva TEL AVIV')
buildingB = Building('112 Edward Street LONDON')
buildingC = Building('rehov HaShalom, 18 JERUSALEM')
buildingD = Building('68, rue de Paris PARIS')
buildingE = Building('Colombus Circle LONDON')


human1.move(buildingA)
human3.move(buildingA)

print(buildingA.inhabitants_name())
print(buildingB.inhabitants_name())

print(buildingD.address)
print(human1)
print(human3)
print(human1.living_place)
print(human4.name)
human4.move(buildingD)
print(human4.living_place, ' to be compared with', buildingD)
human5.move(buildingD)
print(human5.living_place.address) # why highlighted whereas it works
print(human5.living_place)
human6.move(buildingC)
human7.move(buildingC)
human8.move(buildingC)
print(buildingD.inhabitants_name())
print(vars(buildingD))
print(Building.buildings_list)
print(buildingA.inhabitants_name())
print(buildingA.inhabitants_name())


london = City('London')
london.construct('10 Downing street')
london.construct('Colombus Circle')
print(london.buildings)
print(london.buildings_addr())

human9.move(buildingE)
human10.move(buildingE)
print(london.info())

"""buildingA = Building('rehov HaTikva TEL AVIV', [human1, human3]) 
buildingB = Building('112 Edward Street LONDON', [human2]) 
buildingC = Building('rehov HaShalom, 18 JERUSALEM', [human6, human7, human8]) 
buildingD = Building('68, rue de Paris PARIS', [human4, human5]) 
buildingE = Building('Colombus Circle LONDON ', [human9, human10]) 
"""


