# Exercise 1
import re

def return_numbers(text):
    return1 = ''.join(filter(str.isdigit, text))
    return2 = ''.join(re.findall(r'\d+', text))
    return3 = [int(s) for s in re.findall(r'\d+', text)]
    print(return2)
    return return2


return_numbers('k5k3q2g5z6x9bn')

# Exercise 2


def check_name(name):
    #name = input('Please enter you first and last names (example : \"John Doe\"') as a comment for testing below
    if not re.match(r"([A-Z]{1}[a-z]{1,}\s([a-zA-Z]{1}')?([A-Z]{1}[a-z]{1,}))", name):
        return False
    else:
        return True

#Testing


print(check_name('John Doe'))
print(check_name("John D'Oe"))
print(check_name("John d'Oe"))
print(check_name("John MacDoe"))
print(check_name("John DOe")) #False
print(check_name("John D")) #False
print(check_name("John doe")) #False
print(check_name("john Doe")) #False


# Exercise 3


import random
import string


def check_password(password):
   pattern = r'^[0-9]+[A-Z]+[a-z]+'
   special_list = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 152)]
   special_in_password = [position for position, char in enumerate(password) if char in special_list]
   if len(special_in_password) != 0:
       for i in special_list:
           password = password.replace(i, "")
       sorted_password = ''.join(sorted(password))
       check = re.compile(pattern)
       if check.match(sorted_password) is not None:
           valid = True
       else:
           valid = False
   else:
       valid = False
   print(valid)
   return valid


def generate_password(length):
    char_list = [chr(i) for i in range(33, 127)]
    password = ''
    iterate = True
    while iterate:
        password = ''.join(random.choice(char_list) for i in range(length))
        if check_password(password):
            break
    return password


def generate_sample(num):
    sample = []
    for i in range(num):
        length = random.randint(6, 31)
        password = generate_password(length) # same test for generating and testing so no surprise !!
        sample.append(password)
    print(sample)
    return sample


sample = generate_sample(100)
check_password(sample[99]) # same test for generating and testing so no surprise, by construction all are valid !

def your_good_password():
    length = 0
    while length not in range(6, 31):
        length = int(input('What length do you want for your password? Please enter a number between 6 and 30: '))
    password = generate_password(length)
    print(f'This is your secret password: {password}.\nPlease keep it in safe place.')
    return password


your_good_password()