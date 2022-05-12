# Exercise 7

from datetime import datetime
from datetime import date


def get_birthdate():
    birthdate_string = input('Please input your birthdate (YYYY/MM/DD) : ')
    birthdate = datetime.strptime(birthdate_string, "%Y/%m/%d")
    return birthdate


def get_gender():
    gender = input('Please input your birthdate (\'m\' or \'f\') : ')
    return gender


def get_age():  # Sorry but leap years will be tackled another day!
    birthdate = get_birthdate()
    today = date.today()
    age = today.year - birthdate.year - (
            (today.month, today.day) < (birthdate.month, birthdate.day))  # the latter is 1 if True
    return age


def can_retire():
    age = get_age()
    gender = get_gender()
    p = [age, gender]
    # How to do the following lines in a one-liner ?
    if (p[0] >= 67 and p[1] == 'm') or (p[0] >= 62 and p[1]) == 'f':
        can_retire_bool = True
    else:
        can_retire_bool = False
    print(can_retire_bool)


can_retire()
