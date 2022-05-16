# DAILY CHALLENGE

class Farm:

    def __init__(self, name):
        self.name = name
        self.animals = {}
        self.animals['cow']= 2
        print(self.animals)



    def add_animal(self, animal, number = 1):
        #self.animals[animal] += number
        for key, value in self.animals.items():
            if animal != key:
                self.animals[animal].append(number)
            elif animal == key:
                self.animals[animal] += number
        print(self.animals)


    def get_info(self):
        print(f'{self.name}\' farm')
        for key, value in self.animals.items():
            print(f'{key} : {value}')
        print('E-I-E-I-O')


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())




