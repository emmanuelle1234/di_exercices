# EXERCISE 1

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Felix', 2)
cat2 = Cat('Tigger', 0.5)
cat3 = Cat('Lily', 7)
cats = {
        cat1.name: cat1.age,
        cat2.name: cat2.age,
        cat3.name: cat3.age
}
print(cats)


def is_the_oldest(cats):
    c_list = [age for key, age in cats.items()]
    for i in range(len(c_list) - 1):
        minimum = i
        for j in range(i + 1, len(c_list)):
            if c_list[j] < c_list[minimum]:
                minimum = j
                if (
                        minimum != i):
                    c_list[i], c_list[minimum] = c_list[minimum], c_list[i]
    oldest = c_list[len(c_list) - 1]
    return oldest


oldest_name = list(cats.keys())[list(cats.values()).index(is_the_oldest(cats))]

print(f'The oldest cat is {oldest_name} and is {is_the_oldest(cats)} years old')


# EXERCISE 2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print("{} goes woof!".format(self.name))

    def jump(self):
        print("{} jumps {} cm high!".format(self.name, self.height*2))


davids_dog = Dog("Rex", 50)

print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    bigger = davids_dog
else:
    bigger = sarahs_dog

print(bigger.name)

print("")
# EXERCISE 3


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)


stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


print("")
# EXERCISE 4


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animals(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals_list = sorted(self.animals)
        sorted_animals_dict = {
            1: 'a'
        }
        for i in range(len(sorted_animals_list)):
            sorted_animals_dict[i][i] = i+1
            print(sorted_animals_dict[i][0])
            sorted_animals_dict[i][1] = sorted_animals_list[i]
            print(sorted_animals_dict[i][1])
            i#f sorted_animals_list[i][0] not in
                #sorted_animals_dict[1] = i
        print(sorted_animals_dict)


zoo1 = Zoo("Thoiry")
zoo1.add_animals("Emu")
zoo1.add_animals("Giraffe")
zoo1.add_animals("Snake")
zoo1.add_animals("Cougar")
zoo1.add_animals("Bear")
zoo1.add_animals("Ape")
zoo1.add_animals("Cat")
zoo1.add_animals("Baboon")
zoo1.add_animals("Eel")
zoo1.get_animals()
zoo1.sell_animal('Snake')
zoo1.get_animals()
zoo1.sort_animals()




