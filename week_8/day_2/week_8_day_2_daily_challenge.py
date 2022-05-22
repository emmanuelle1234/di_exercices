# DAILY CHALLENGE

class Farm:

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number=1):
        item = {animal: number}
        if animal not in self.animals.keys(): # here we can do just animal not in self.animals
            self.animals.update(item)
        else:
            self.animals[animal] += number

    def get_info(self):
        print(f'{self.name}\' farm')
        print('')
        for key, value in self.animals.items():
            print(f'{key} : {value}')
        print('')
        print('   E-I-E-I-O!') # rather than spaces you can create tab by \t
        return ""


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

class Door:

    def __init__(self):
        self.is_opened = False

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

class BlockedDoor (Door):

    def open_door(self):
        raise Exception('not possible to open a blocked door')

    def close_door(self):
        print('Error')
        raise Exception('not possible to open a blocked door')

a = BlockedDoor()
class Door:
	def __init__(self, is_opened):
		self.is_opened = is_opened
		if is_opened == True:
			print('The door is open')
		else:
			print('The door is closed')

	def open_door(self):
		self.is_opened = True

	def close_door(self):
		self.is_opened = False

	def status(self):
		if self.is_opened == True:
			print("the door is opened")
		else:
			print("the door is closed")


class BlockedDoor(Door):
	def open_door(self):
		raise Exception('Blocked door cannot be opened or closed')

	def clos
