# WEEK 7 DAY 1

numbers = [1, 2, 3, 4]
for index, number in enumerate(numbers):
    numbers[index] = number * 3


# passing by value
def calculation1(value):
    return value + 5


a = 2
print(f"before: {a}")
print(f"res: {calculation1(a)}")
print(f"after: {a}")


# passing by reference
def calculation2(list_of_numbers):
    for index in range(0, len(list_of_numbers)):
        list_of_numbers[index] += 5
    return list_of_numbers


numbers = [40, 50, 60]
print(f"before: {numbers}")
res = calculation2(numbers)
print(f"res: {res}")
print(f"after: {numbers}")

numbers2 = [40, 50, 60]
print(f"before: {numbers2}")
res = calculation2(numbers2.copy()) # to have the original list unchanged
print(f"res: {res}")
print(f"after: {numbers2}")

# list of functions

def add(num):
    print(num + 2)

def sub(num):
    print(num - 2)

def mul(num):
    print(num * 2)

number = 3
functions = [add, sub, mul]

for fct in functions:
    fct(number)

# set of numbers
"""
1. Not sequenced => no order => access by value NB:in Python 3.10 only, new element is added at the end
2. Mutable (see after)
"""

# about testing: unittest ?