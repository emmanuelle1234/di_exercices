"""Week6 Day2 Daily Challenge

Instructions
1. Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
2. Then, print the first and last characters of the given text.
3. Construct the string character by character: Print the first character, then the second, then the third,
until the full string is printed. For example:
The user enters "Hello World"
Then, you have to construct the string character by character
H
He
Hel
... etc
Hello World
4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).
For example:
Hlrolelwod
"""
import random

answer1 = input('Please enter a 10 characters string: ')
length1 = len(answer1)
answer2=answer1.replace(" ","")
if len(answer2) < 10:
    print('string not long enough')
if len(answer2) > 10:
    print('string too long')
print (answer1[0] + answer1[1])
#letters list depends on the number of spaces
letters_list = list(answer1)
construct ="";
print(construct)
for x in letters_list:
    construct = construct + x
    print(construct)

letters_list2 = list(answer2)
random.shuffle(letters_list2)
shuffled_answer = ''.join(letters_list2)
print(shuffled_answer)








