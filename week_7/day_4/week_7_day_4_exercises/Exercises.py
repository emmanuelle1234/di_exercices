
# EXERCISE 1: TEMPERATURE ADVICE
import random
import datetime





def get_random_temp(season):
    (a, b) = ('', '')
    if season == 'winter':
        a, b = (-10, 16)
    elif season == 'spring':
        a, b = (-1, 32)
    elif season == 'summer':
        a, b = (10, 40)
    elif season in ['autumn', 'fall']:
        a, b = (0, 27)
    return random.randint(a, b)


print(get_random_temp('summer'))  # just to test


def user_month():
    the_season = ''
    month = input('Please enter a month (eg. 1 for January, 12 for December): ')
    if month in ['12', '1', '2']:
        the_season = 'winter'
    elif month in ['3', '4', '5']:
        the_season = 'spring'
    elif month in ['6', '7', '8']:
        the_season = 'summer'
    elif month in ['9', '10', '11']:
        the_season = 'autumn'
    return the_season


def custom_message_generate(temp):
    if temp < 0:
        message = "Brrr, that’s freezing! Wear some extra layers today"
    elif temp < 16:
        message = "Quite chilly! Don’t forget your coat"
    elif temp < 24:
        message = "What a cool weather!"
    elif temp < 32:
        message = "Don't forget to protect against sun rays"
    else:
        message = "Think to drink water! "
    return message


def user_season():
    season = input('Please enter a season: ')
    return season


def main():
    # random_temp= get_random_temp(user_season())
    random_temp = get_random_temp(user_month())
    print(f'Hello, the temperature right now is {random_temp} degrees Celsius')
    print(custom_message_generate(random_temp))


main()

print('\n')
# EXERCISE 2


def get_birthdate():
    birthdate_string = input('Please input your birthdate (YYYY/MM/DD) : ')
    birthdate = datetime.datetime.strptime(birthdate_string, '%Y/%m/%d')
    return birthdate


def get_gender():
    gender = input('Please input your gender (\'m\' or \'f\') : ')
    return gender


def get_age():  # Sorry but leap years will be tackled another day!
    birthdate = get_birthdate()
    today = datetime.date.today()
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


# EXERCISE 3


def func(X):
    return X + int(str(X)*2)+int(str(X)*3)+int(str(X)*4)


print(func(3))

