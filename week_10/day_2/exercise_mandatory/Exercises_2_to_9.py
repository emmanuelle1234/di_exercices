# EXERCISE 2
from random import randint


def compare_with_random(num):
    assert num in range(1, 101)
    if num == randint(1, 100):
        message = "Success"
        print(message)
        return message
    else:
        print('lost')


# TESTING

compare_with_random(2)
"""compare_with_random(201)"""


# EXERCISE 3
from string import ascii_lowercase, ascii_uppercase
from random import choice

def generate_random_string(len):
    letters = ascii_lowercase + ascii_uppercase
    random_string = ''.join(choice(letters) for i in range(len))
    print(f"Random string of length {len}: {random_string}")

# TESTING


generate_random_string(5)
generate_random_string(6)

# EXERCISE 4
from datetime import date


def today():
    today_date = date.today()
    print(today_date)


today()

# EXERCISE 5
from datetime import datetime

def until():

    current_datetime = datetime.now()
    current_year = date.today().year
    january_1st = datetime(current_year+1, 1, 1, 0, 0, 0)
    delta = january_1st - current_datetime
    delta_s = delta.seconds # datetime.hours and minutes does not exist ?
    minutes, seconds = divmod(delta_s, 60)
    hours, minutes = divmod(minutes, 60)

    print(f'The 1st of January is in {delta.days} days and {hours}:{minutes}:{seconds} hours')


until()


# EXERCISE 6

def minutes_lived(birthday: date):
    current_datetime = datetime.now()
    delta = current_datetime - birthday
    delta_in_mn = delta.days*24*60 + int(delta.seconds/60)
    print(f'Today you have already lived {delta_in_mn} minutes in your life.')


minutes_lived(datetime(2022, 1, 1, 0, 0, 0))

# EXERCISE 7


def time_to_holidays():
    current_datetime = datetime.now()
    current_day = date.today
    print(f'Today is {current_datetime.strftime("%Y-%m-%d")}')
    next_holidays = datetime(2022,7,1)
    delta = next_holidays - current_datetime
    delta_s = delta.seconds  # datetime.hours and minutes does not exist ?
    minutes, seconds = divmod(delta_s, 60)
    hours, minutes = divmod(minutes, 60)
    print(f'The next holiday is in {delta.days} days and {hours}:{minutes}:{seconds} hours')

time_to_holidays()


# EXERCISE 8

#Not understood really the aim of the exercise in relationship with modules
def old(age_in_s, planet):
    age_earth = age_in_s/31557600
    if planet == 'Earth':
        coeff1 = 1
    elif planet == 'Mercury':
        coeff1 = 0.2408467
    elif planet == 'Venus':
        coeff1 = 0.61519726
    elif planet == 'Mars':
        coeff1 = 1.8808158
    elif planet == 'Jupiter':
        coeff1 = 11.862615
    elif planet == 'Saturn':
        coeff1 = 29.447498
    elif planet == 'Uranus':
        coeff1 = 84.016846
    elif planet == 'Neptune':
        coeff1 = 164.79132, 2
    else:
        coeff1 = 1
    print(f'You are {age_in_s}-seconds old, so you are {round(age_earth * coeff1, 2)} {planet}-years old.')

old(1000000000, 'Earth')


# EXERCISE 9
"""
Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: 
name, address, language_code. Use faker to populate them with fake data."""

from faker import Faker
users = []

def add_user(num):
    for i in range(num):
        fake = Faker()
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
         }
        users.append(user)


add_user(4)
print(users)