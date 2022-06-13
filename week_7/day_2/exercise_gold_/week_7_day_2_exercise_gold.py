# EXERCISE :

from random import randint


def throw_dice():
    return randint(1, 6)


def throw_until_doubles():
    both_same = False
    count = 0
    while not both_same:
        count += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice2 == dice1:
            break
    return count

print(throw_until_doubles())

def main():
    counter = 0
    for i in range(1, 100):
        counter += throw_until_doubles()
    return counter


total = main()

print(f'''
Total throws: {total}
Average throws to reach doubles: {total/100}
''')

