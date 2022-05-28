class Person:
    def __init__(self, person_name, like=[], hate=[]):
        self.person_name = person_name
        self.like = like
        self.hate = hate

    def taste(self, food_name):
        message = f'{self.person_name} eats the {food_name}'
        if food_name in self.like:
            message = message + ' and loves it!'
        elif food_name in self.hate:
            message = message + ' and hates it!'
        else:
            message = message + '!'
        print(message)


p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream")
p1.taste("cheese")
p1.taste("carrots")

