#Exercise 1
#Write a script that inserts an item at a defined index in a list.
import math


def script(item, index, my_list):
    my_list.insert(index, item)
    return my_list

print(script({'key': 'value'}, 2, [[0, 0], 'b', 3, (0, 0)]))


#Exercise 2
#Write a script that counts the number of spaces in a string.

def spaces_counter(string):
    counter = 0
    for i in string:
        if(i.isspace()):
            counter += 1
    return counter

print(spaces_counter("This text is full of empty spaces but how much?"))

#Exercise 3
#Write a script that calculates the number of upper case letters and lower case letters in a string.


def letter_types_counter(string):
    upper_counter = 0
    lower_counter = 0
    for i in string:
        if i.isupper():
            upper_counter += 1
        elif i.islower():
            lower_counter += 1
        else:
            pass
    return f'Number of upper case letters is {upper_counter} and number of lower case letters is {lower_counter}'


print(letter_types_counter("This Text is Full of Empty Spaces but how much?"))

#Exercise 4
# Write a function to find the sum of an array (list ?) without using the built-in function:

def my_sum(my_list):
    counter = 0
    for index in range(len(my_list)):
        counter += my_list[index]
    return f'Sum of the items in {my_list} is {counter}'

print(my_sum([1, 2, 3, 4]))

#Exercise 5
#Write a function to find the max number in a list


def find_max(my_list):
    max = my_list[0]
    for i in range(1, len(my_list)-1):
        if my_list[i+1] > max:
            max = my_list[i+1]
    return max


print(find_max([0, 1, 3, 50]))


#Exercise 6
#Write a function that returns factorial of a number

def factorial(num):
    facto = 1
    for i in range(1, num):
        facto = facto * (i+1)
    return facto


print(factorial(4))

#Exercise 7
#Write a function that counts an element in a list (without using the count method)

def list_count(my_list, element):
    counter = 0
    for item in my_list:
        if item ==  element:
            counter += 1
    return counter


print(list_count(['a','a','t','o'],'a'))

#Exercise 8
#Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:


def norm(my_list):
    counter = 0
    for index in range(len(my_list)):
        counter += my_list[index] * my_list[index]
    return math.sqrt(counter)


print(norm([1,2,2]))

#Exercise 9
#Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono(my_list):
    if all(x >= y for x, y in zip(my_list, my_list[1:])):   # aggregates in tuples (each item except the first and the last is
                                                            # in 2 tuples) and compares diff sign for  each tuple
                                                            #print(list(zip(my_list, my_list[1:])))
        return True
    elif all(x <= y for x, y in zip(my_list, my_list[1:])):
        return True
    else:
        return False


print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))

#Exercise 10
#Write a function that prints the longest word in a list.

def longest(my_list):
    max = len(my_list[0])
    word = my_list[0]
    for i in range(len(my_list)):
        # print(len(my_list[i]))
        if len(my_list[i]) > max:
            max = len(my_list[i])
            word = my_list[i]
    return word

print(longest(['hahaha', 'anticonstitutionnellement', 'tired', 'toomuchexerciseshere']))


#Exercise 11
#Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def types_sort(my_list):
    int_list = []
    str_list = []
    for i in range(len(my_list)):
        if type(my_list[i]) == int:
            int_list.append(my_list[i])
        elif type(my_list[i]) == str:
            str_list.append(my_list[i])
        else:
            pass
    return [int_list, str_list]

print(types_sort([2, '2', 3, 'list', 'number', 4]))

#Exercise 12
#Write a function to check if a string is a palindrome:

def is_palindrome(string):
    list_a = list(string.replace(" ", "").upper())
    reverse_list = list_a[::-1]
    if string.upper() == "".join(reverse_list):
        return True
    else:
        return False

print(is_palindrome('John'))
print(is_palindrome('Anna'))
print(is_palindrome('radar'))
print(is_palindrome('rotor'))
print(is_palindrome('test'))

#Exercise 13
#Write a function that returns the amount of words in a sentence with length > k:


def sum_over_k(sentence, k):
    sentence_list = sentence.split(" ")
    if len(sentence_list) > k:
        return len(sentence_list)


sentence = 'Do or do not there is no try'
k = 2
print(sum_over_k(sentence, k))

#Exercise 14
#Write a function that returns the average value in a dictionary (assume the values are numeric):

def dict_avg(my_dict):
    counter = 0
    my_sum = 0
    for k, v in my_dict.items():
        counter += 1
        my_sum += my_dict[k]
    return my_sum/counter

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

#Exercise 15
#Write a function that returns common divisors of 2 numbers:

def common_div(x, y):
    x_div = []
    y_div = []
    for i in range(2, x+1):
        if x%i == 0:
            x_div.append(i)
    for i in range(2, y+1):
        if y%i == 0:
            y_div.append(i)
    return list(set(x_div).intersection(y_div))


print(sorted(common_div(10, 20)))

#Exercise 16


def is_prime(x):
    x_div = []
    for i in range(1, x+1):
        if x%i == 0:
            x_div.append(i)
    if len(x_div) < 3:
        return True
    else:
        return False


print(is_prime(11))
print(is_prime(15))

#Exercise 17
# Write a function that prints elements of a list if the index and the value are even:
def weird_print(my_list):
    weird = []
    for i in range(len(my_list)):
        if i%2 == 0 and my_list[i]%2 == 0:
            weird.append(my_list[i])
    return weird

print(weird_print([1,2,2,3,4,5]))

#Exercise 18
#Write a function that accepts an undefined number of keyworded arguments and return the count of different types:


def type_count(**kwargs):
    int_count = 0
    str_count = 0
    fl_count = 0
    bool_count = 0
    for key, value in kwargs.items():
        if type(value) == int:
            int_count += 1
        elif type(value) == float:
            fl_count += 1
        elif type(value) == bool:
            bool_count += 1
        elif type(value) == str:
            str_count += 1
    return f'int: {int_count}, str: {str_count} , float: {fl_count}, bool: {bool_count}'


print(type_count(a=1, b='string', c=1.0, d=True, e=False))


#Exercise 19
#Write a function that mimics the builtin .split() method for strings.
#By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.


def newsplit(string, separation=" "):
    string_list = []
    item = ""
    if not isinstance(string, str):
        return "not a string"
    for index, letter in enumerate(string):
        if index == string.rfind(separation) + 1: # the last word cannot be identifed with a space at the end by construction. l
                                            # last occurrence of space so start of last word
            item = string[index:] # item to append to the list = last word
            string_list.append(item)
            item = ""
        elif letter != separation: # take letters to constitute a word
            item += letter
        else: # space, so the item is a word
            string_list.append(item)
            item = ""
    return string_list


print(newsplit("uplou ou zz"))
print(newsplit("uplou,ou,zz", ","))
# remains to be improved if separation is more than one char

#Exercise 20
#Convert a string into password format.


def passw(string):
    return len(string)*"*"


print(passw("mypassword"))
