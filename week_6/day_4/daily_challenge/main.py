# Week6 Day4 Daily Challenge

import datetime

birth_date = input("Please enter your birthdate (YYYY-mm-dd):")
birth_date=datetime.datetime.strptime(birth_date,'%Y-%m-%d')
today = datetime.date.today()
age = today.year - birth_date.year -((today.month, today.day) < (birth_date.month, birth_date.day))
x=int(repr(age)[-1]) #last digit

for last_digit in range(0,9):
        l1 = f'{"_"*int((11-x)/2)}{"i"*x}{"_"*(11-x-int((11-x)/2))}'

cake2=f'    {l1}  \n   |:H:a:p:p:y:|  \n __|{"_"*11}|__ \n|{"^"*17}|\n|:B:i:r:t:h:d:a:y:|\n|{" "*17}|\n{"~"*19}\n'

if birth_date.year%4==0 and birth_date.year%100!=0 or birth_date.year%400==0:
    print(cake2 *2)
else: print(cake2)





