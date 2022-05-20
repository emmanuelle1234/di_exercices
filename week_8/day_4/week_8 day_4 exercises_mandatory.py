# Exercise 1 :
import random


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Persian('Persy', 3)
cat2 = Chartreux('Char', 1)
cat3 = Bengal('Ben', 7)

my_cats = [cat1, cat2, cat3]

my_pets = Pets(my_cats)

my_pets.walk()


# Exercise 2 :


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        print(f'{self.name}\'s running speed is {self.weight/self.age*10}')
        return self.weight/self.age*10

    def fight(self, other_dog):
        winner = self.name if self.run_speed() > other_dog.run_speed() else other_dog.name
        print(f'The winner is {winner}')


dog1 = Dog("Doudou", 3, 10)
dog2 = Dog("Bella", 1, 4)
dog3 = Dog("Waffy", 4, 20)

dog1.bark()
dog2.run_speed()
dog3.fight(dog2)
dog2.fight(dog3)


# Exercise 3 :

"""Instructions
Create a new python file and import your Dog class from the previous exercise. ???
In the new python file, create a class named PetDog that inherits from Dog.
Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
Add the following methods:
train: prints the output of bark and switches the trained boolean to True

play: takes a parameter which value is a few names of other dogs (use *args). g string: “dog_names all play together”.

do_a_trick: If the dog is trained the method should print one of the following sentences at random:
“dog_name does a barrel roll”.
“dog_name stands on his back legs”.
“dog_name shakes your hand”.
“dog_name plays dead”."""



class PetDog(Dog):

    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(i for i in args)
        print(f'{dog_names} all play together')

    def do_a_trick(self):
        messages = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead' ]
        random_num = random.randint(0,4)
        if self.trained:
            print(f'{self.name} {messages[random_num]}')


doggy = PetDog('Doggy', 1, 12)
print(doggy.trained)
doggy.train()
print(doggy.trained)
doggy.play('Fifi', 'Loulou', 'Riri')
doggy.do_a_trick()
