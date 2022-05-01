# Exercise 1
#zip() pairs the list element with other list element at corresponding index in form of keu-value pairs.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
num_dict=dict(zip(keys, values))
print(str(num_dict))

# Exercise 2
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family = {}
total_cost=0
family_members = int(input('Please enters the number of the members in the family: '))
for i in range(family_members):
    cost = 0
    name = input('Please enter your first name: ')
    age = input('Please enter your age: ')
    if int(age) < 3:
        print('You don\'t have to pay')
        family.update({name: [int(age), 0]})
    elif int(age) <= 12:
        print('Your ticket is $10')
        family.update({name: [int(age), 10]})
    else:
        print('Your ticket is $15')
        family.update({name: [int(age), 15]})
print(family)
for k,v in family.items():
    total_cost+=v[1]
print(f'The total cost for your family is ${total_cost}')

#Exercise 3

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']}
}
print(brand["major_color"].keys())

brand['number_stores']=2
# or : brand.update({'number_stores': 2});

countries_list=[]
for key in brand['major_color']:
    countries_list.append(key)
countries_string=', '.join(countries_list)
print(countries_string)
clothes = ", ".join(brand["type_of_clothes"][:3])
other = "".join(brand["type_of_clothes"][3])

print(f'{brand["name"]}\'s clients are in {countries_string}. They look for clothes for {clothes} and products for {other}.')

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')

del brand['creation_date']

print(brand["international_competitors"][len(brand["international_competitors"])-1])

US_major_colors=", ".join(brand["major_color"]["US"])
print(US_major_colors)

print(len(brand.items()))

for k in brand.items():
    print(k[0])

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara)
print(brand)

print(brand["number_stores"])
#The value was replaced when adding the information from the more_on_zara dictionary because the key already existed in the brand dictionary.

#Exercise 4
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

#1/Recreate using a loop
""">>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}"""
disney_users_A = {}
for count, value in enumerate(users):
    disney_users_A[value] = count
print(disney_users_A)
#2/
""">>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}"""
disney_users_B = {}
for count, value in enumerate(users):
    disney_users_B[count] = value
print(disney_users_B)


#3/
""">>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}"""
#for the pleasure to complicate
disney_users=sorted(users)
disney_users_C_reverse={}
for i in range (0, len(disney_users)):
    disney_users_C_reverse[i]=disney_users[i]
disney_users_C= {value : key for (key, value) in disney_users_C_reverse.items()}
print(disney_users_C)

#4/
char="i"
disney_users_A_i= {key: value for key, value in disney_users_A.items() if char in key}
print(disney_users_A_i)
disney_users_A_mp = {key: value for key, value in disney_users_A.items() if key[0]=="M" or key[0]=="P"}
print(disney_users_A_mp)
