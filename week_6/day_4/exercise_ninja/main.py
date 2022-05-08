# Exercise 1
import math
D= 0
C = 50
H = 30
parameters= input("Please enter a comma-separated string of numbers: ")
D_list = parameters.split(",")
Q_list =[]
for i in range(0, len(D_list)):
    D=int(D_list[i])
    Q = int(math.sqrt((2 * C * D) / H))
    Q_list.append(Q)
print(Q_list)

# Exercise 2
#1
list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
list5=[1, 3, 5, 1, 3, 5]
#2a
string_list1 = [str(item) for item in list1]
print(string_list1)
print(", ".join(string_list1))
#2b
reverse_sorted_list1=sorted(list1, reverse=True)
print (reverse_sorted_list1)
#2c
sum=0
for i in range(len(list1)):
    sum = sum+list1[i]
print(sum)
#3 assumption : the first (resp. last) number means the number in the first (resp. last) position in the initial list
list_first_last =[]
list_first_last.append(list1[0])
list_first_last.append(list1[len(list1)-1])
print(list_first_last)
#4
new1_list1 =[]
for i in range(0, len(list1)):
    if list1[i]>50:
        new1_list1.append(list1[i])
        new1_list1.sort()
print(new1_list1)
#5
new2_list1 =[]
for i in range(0, len(list1)):
    if list1[i]<10:
        new2_list1.append(list1[i])
        new2_list1.sort()
print(new2_list1)
#6
squared_list1 =[]
for i in range(0, len(list1)):
    squared_list1.append(list1[i]*list1[i])
print(squared_list1)
#7
without_duplicate_list5=list(set(list5))
print(without_duplicate_list5)
#8
average=sum/len(list1)
print(average)
#9
print(reverse_sorted_list1[0])
#10
sorted_list1=sorted(list1)
print (sorted_list1[0])
#11 already done
#12
list=[]
while len(list)<10:
    number =input("Plesase input one integer between -100 and 100: ")
    list.append(number)


string_list = [str(item) for item in list]
print(string_list)
print(", ".join(string_list))
#And afterwatds, as beyond
reverse_sorted_list=sorted(list, reverse=True)
print (f"The reverse sorted list is: {reverse_sorted_list}"
)
# etc...


#Exercise 3: Working On A Paragraph

textb="Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)" \
     "\nPaste it to your code, and store it in a variable." \
     "\nLet’s analyze the paragraph. Print out a nicely formatted message saying:" \
     "\nHow many characters it contains (this one is easy…)." \
     "\nHow many sentences it contains." \
     "\nHow many words it contains." \
     "\nHow many unique words it contains."\
     "\nBonus: How many non-whitespace characters it contains." \
     "\nBonus: The average amount of words per sentence in the paragraph." \
     "\nBonus: the amount of non-unique words in the paragraph."
text='the amount of'
print(text)
print(f'This text contains {len(text)} characters.')

import re

sentences_number=len(re.split(r'[.!?]+', text))
print(f'The number of sentences this text contains is {sentences_number}.')

words=re.findall(r'\w+', text)
words_number = len(re.findall(r'\w+', text))
print(f'The number of words this text contains is {words_number}.')

unique_words_number = len(set(words))
print(f'According to a first method, the text contains {unique_words_number} unique words.')

from collections import Counter
unique_words_number2 = len(Counter(words).keys())
print(f'According to a second method, the text contains {unique_words_number2} unique words.')

non_whitespace_characters_text=[char for char in text if not char.isspace()] # or : char.split()
print(f'This text contains {len(non_whitespace_characters_text)} characters without taking into account whitespaces.')


#Exercise 4
text="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
frequency = Counter(text.split()).most_common()
print(frequency)
for word, count in frequency:
    print(f'{word}:{count}')

