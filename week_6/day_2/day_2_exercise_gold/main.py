# Exercises XP

# Exercise 1
print('Hello world\n'*4 + 'I love python\n'*4)

# Exercise 2
"""Instructions
1. Ask the user to input a month (1 to 12).
2. Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)"""

month = int(input('Please enter a month with a number from 1 to 12: '))
if month >= 3 and month < 6:
    print('spring')
if month >= 6 and month < 9:
    print('summer')
if month >= 9 and month < 12:
    print('automn')
if month == 12 or month < 3:
    print('winter')

