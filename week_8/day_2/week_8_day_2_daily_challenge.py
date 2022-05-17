# DAILY CHALLENGE

class Farm:

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number=1):
        item = {animal: number}
        if animal not in self.animals.keys():
            self.animals.update(item)
        else:
            self.animals[animal] += number

    def get_info(self):
        print(f'{self.name}\' farm')
        print('')
        for key, value in self.animals.items():
            print(f'{key} : {value}')
        print('')
        print('   E-I-E-I-O!')
        return ""


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
