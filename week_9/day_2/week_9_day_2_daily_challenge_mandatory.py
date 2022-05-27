# DAILY CHALLENGE
import math
from operator import itemgetter

class Circle:

    def __init__(self, name, radius):
        self.radius = radius
        self.name = name

    @classmethod
    def create_circle(cls, name):
        what = input(f'Do you want to use diameter or radius to create the circle: ')
        if what == "diameter":
            diameter = int(input('Please enter the size of the diameter: '))
            radius = diameter/2
            print(f'You created a circle with a diameter equal to {diameter} and a radius equal to {radius}')
            return cls(name, radius)
        elif what == "radius":
            radius = int(input('Please enter the size of the radius: '))
            print(f'You created a circle with a radius equal to {radius}')
            return cls(name, radius)
        else:
            raise TypeError('Please enter \'diameter\' or \'circle\' only.')

    def circle_area(self):
        area = math.pi * self.radius * self.radius
        return area

    def circle_print(self):
        return f'As I am not able to draw the circle, I am sure you will be happy to be reminded that :\n' \
               f'the radius is {self.radius} and the diameter is {self.radius *2}.'

    def __add__(self, other):
        result_circle = Circle('added_circle', self.radius + other.radius)
        print(result_circle.radius)
        return result_circle

    def compare(self, other):
        if self.radius > other.radius:
            return f'This circle ({self.name}) is bigger than the other one ({other.name}).'
        elif self.radius < other.radius:
            return f'This circle ({self.name}) is smaller than the other one ({other.name}).'
        else:
            return f'This circle ({self.name}) has the same size as the other one ({other.name}).'

    def add_and_sort_by_name(self, circles_list):
        circles_list.append([self.name, self.radius])
        circles_list.sort(key=lambda x: x[0])
        return circles_list

    def add_and_sort_by_radius(self, circles_list):
        circles_list.append([self.name, self.radius])
        circles_list.sort(key=itemgetter(1))
        return circles_list


circle1 = Circle.create_circle('circle1')
print(circle1.radius)
print(circle1.circle_print())
circle2 = Circle('circle2', 2)
circle3 = circle1 + circle2
print(circle3.radius)
print(circle1.compare(circle2))
circles_list = []
circle1.add_and_sort_by_radius(circles_list)
print(circles_list)
circle2.add_and_sort_by_radius(circles_list)
print(circles_list)
circle3.add_and_sort_by_name(circles_list)
print(circles_list)






