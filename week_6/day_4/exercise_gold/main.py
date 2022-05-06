#Exercise1

list1=['items1_1', 'items1_2', 'items1_3']
list2=['items2_1', 'items2_2', 'items2_3', 'items2_4']
#Method1
list_a=[*list1, *list2]
print(list_a)
#Method2
for i in list2:
 list1.append(i)
print(list1)
#Method3
list1=['items1_1', 'items1_2', 'items1_3']#reset after the apped beyond
list_c=[x for list in [list1, list2] for x in list ]
print(list_c)


#Exercise2
number1 = input('Please enter the 1st number: ')
number2 = input('Please enter the 2nd number: ')
number3 = input('Please enter the 3rd number: ')
if number1>=number2:
    list=[number1, number2]
    if number3>=number1:
        list=[number3, number1, number2]
    elif number3>=number2:
        list = [number1, number3, number2]
    else:
        list = [number1, number2, number3]
else:
    list=[number2, number1]
    if number3>=number2:
        list=[number3, number2, number1]
    elif number3>=number2:
        list = [number2, number3, number1]
    else:
        list = [number2, number1, number3]
print(list[0])
#Better
list=[number1, number2, number3]
sorted_list = sorted(list, reverse=True)
print(sorted_list[0])

#Exercise 3
alphabet_list=[chr(x) for x in range(97,123)]
alphabet_string="".join([letter for letter in alphabet_list])
print(alphabet_string)
for letter in alphabet_string:
        if letter in ['a','e','i','o','u','y']:
            message=f'{letter} is a vowel'
        else:
            message = f'{letter} is a consonant'
        print(message)

#Exercise 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input('Please enter your name:')
if name in names:
    print(names.index(name))

#Exercise 5


print("Dear user, I will ask you for 7 words")
words=[]
for i in range(0,7):
    word = input(f'Please enter the word #{i+1} :')
    words.append(word)
    print(words)
letter = input('Now dear user, could please enter a single letter :')
indexes=[]
for item in words:
    if letter in item:
        index = item.index(letter)
        indexes.append(index)
        print(f'The index of the letter {letter} in the word {item} is: {index}')
    else:
        print(f'This is a friendly message to tell you that the letter {letter} is not in the word {item}.')

#Exercise 6 :
list = [i for i in range(1, 1000001)]
print(min(list))
print(max(list))
print(sum(list))

#Exercise 7 :
import random
import re

sequence_string = ', '.join(str(random.randint(0,100)) for x in range(0,6))
print(sequence_string)


sequence_string= re.sub(",","",sequence_string)
print(sequence_string)

sequence_list=sequence_string.split(' ')
print(sequence_list)

sequence_tuple=tuple(sequence_list)
print(sequence_tuple)

#Exercise 8 :

computer_number=random.randint(1,2)
bool=True
count_won=0
count_lost=0
while bool:
    user_number = int(input('Please input a number from 1 to 9 (including): '))
    if user_number==computer_number:
        print('Winner')
        count_won+=1
    else:
        print('Better luck next time')
        count_lost +=1
    quit=input("If you want to quit, enter \'quit\': ")
    if quit=="quit":
        bool=False
        print(f'Total games won is {count_won} and total games lost is {count_lost}')
        break
    else:
        bool=True

