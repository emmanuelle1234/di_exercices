# TIMED CHALLENGE

from collections import Counter


def find_number(my_string, my_letter):
    counter = Counter(my_string)
    return counter[my_letter]


print(find_number('Programming is cool!', 'o'))