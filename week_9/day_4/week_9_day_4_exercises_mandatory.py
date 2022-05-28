# EXERCISE 1 :

class Building:

    buildings_list = []

    def __init__(self, address: str, inhabitants=[]):
        self.address = address
        self.inhabitants = inhabitants
        self.buildings_list.append([self.address])
        self.inhabitants_list = []

    def inhabitants_name(self):
        for i in self.inhabitants:
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
        self.living_place = building
        building.inhabitants.append(self)

    def __str__(self):
        return f'{self.name} lives at {self.living_place}'


class City:
    def __init__(self, name, buildings=[]):
        self.address = name
        self.buildings = buildings
        self.buildings_addresses = []

    def construct(self, address):
        self.buildings.append(Building(address))

    def buildings_addr(self):
        for i in self.buildings:
            self.buildings_addresses.append(i.address)
        return self.buildings_addresses

    def info(self, address): # to be completed
        pass


# TESTING

human1 = Human('human1', 12)
human2 = Human('human2', 74)
human3 = Human('human3', 27)
human4 = Human('human4', 49)
human5 = Human('human5', 31)
human6 = Human('human6', 3)
human7 = Human('human7', 36)
human8 = Human('human8', 25)

buildingA = Building('rehov HaTikva TEL AVIV')
buildingB = Building('112 Edward Street LONDON')
buildingC = Building('rehov HaShalom, 18 JERUSALEM')
buildingD = Building('68, rue de Paris PARIS')


human1.move(buildingA)
human3.move(buildingA)
print(buildingA.inhabitants_name())
print(buildingB.inhabitants_name()) # what is the problem
print(buildingC.inhabitants_name()) # what is the problem
print(buildingD.inhabitants_name()) # what is the problem

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
print(buildingD.inhabitants_name()) # same issue as beyond
print(vars(buildingD))
print(Building.buildings_list)
print(buildingA.inhabitants_name()) # same issue as beyond


london = City('London')
london.construct('10 Downing street')
print(london.buildings)
print(london.buildings_addr())

"""buildingA = Building('rehov HaTikva TEL AVIV', [human1, human3]) 
buildingB = Building('112 Edward Street LONDON', [human2]) 
buildingC = Building('rehov HaShalom, 18 JERUSALEM', [human6, human7, human8]) 
buildingD = Building('68, rue de Paris ', [human4, human5]) 
"""

"""    @classmethod
    def create_building(cls):
        building_input = input(f"Please enter the address : ")
        building_object = Building(building_input)
        return cls(building_object)"""
