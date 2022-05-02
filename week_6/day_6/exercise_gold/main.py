# Exercise 1
import datetime

birthdays={
    "Esther": '1995/09/11',
    "Séphora": '1994/09/11',
    "Haya": '1996/09/11',
    "Tsipora": '1997/09/11',
    "Zipora": '1998/09/11'
}

print('Here are the names of the persons whose birth date is known:\n'
      f'{", ".join(birthdays.keys())}\n')

new_name=input('Hellooo ! We need your help. Please add in our database a new birthday. Thanks to first input the person\'s name: ' )
if new_name in birthdays.keys():
    print('This name is already in our database')
else:
    new_birthdate = input(f'Please enter {new_name} birthday date (format : YYYY/MM/DD): ')
    birthdays[new_name] = new_birthdate

print('Welcome. You can look up the birthdays of the people in the list!')
name = input( 'Please enter a name: ')
if name in birthdays.keys():
    print(f'Happy to provide you with {name}\'s birthday date!')
    print(f'The ')
    x=len(name)
    format = '%Y/%m/%d'
    birthdate=str(datetime.datetime.strptime(birthdays[name], format).date())
    y=len(f'on {birthdate}')
    l1= f'|{" " * int((17 - x) / 2)}{name}{" " * (17 - x - int((17 - x) / 2))}|'
    l2= f'|{" " * int((17 - y) / 2)}on {birthdate}{" " * (17 - y - int((17 - y) / 2))}|'
    cake = f'    {"_"*11}  \n   |:H:a:p:p:y:|  \n __|{"_" * 11}|__ \n|{"^" * 17}|\n|:B:i:r:t:h:d:a:y:|\n{l1}\n{l2}\n|{" " * 17}|\n{"~" * 19}\n'
    print(cake)
else:
    print(f'Sorry, we don\'t have the birthday information for {name}')

# Exercise 4

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(f'Dear customers, we are so proud to propose you fruits at the following unbeatable prices (in USD) :')
sentence=str(items).replace("{","").replace("}","").replace("'","")
print(sentence)

for k,v in items.items():
    items[k] ={v, int(input(f'How many {k}(s) in stock ? '))} #would have prefered a list!!
print(items)

cost=0
for i in items.values():
    j=list(i)
    cost = cost + j[0] * j[1]
print(items)

print(f'The value of the stock is ${cost}')


# Exercise 5

cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars_list = "".join(cars_string).split(', ')
print(f'There are {len(cars_list)} manufacturers')
cars_list_reverse = sorted(cars_list, reverse=True)
print(f'The list of manufacturers in descending order is {cars_list_reverse}')
cars_list_o=[item for item in cars_list if 'o' in item ]
print(f'There are {len(cars_list_o)} manufacturers with the letter \'o\' in their name')
cars_list_not_i=[item for item in cars_list if 'i' not in item ]
print(f'There are {len(cars_list_not_i)} manufacturers without the letter \'i\' in their name')



cars_list2 = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars_set = set(cars_list2)
print(f'Here is the list without duplicates: {", ".join(cars_set)}.\n'
      f'There are {len(cars_set)} companies in this list.')
