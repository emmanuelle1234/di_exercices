# EXERCISE : TEMPERATURE ADVICE
import random


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
