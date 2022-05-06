# Timed exercise 1: perfect number

x = int(input('Enter the number: '))
divisors = [i for i in range(1, x) if x % i == 0]
my_sum = 0
print(divisors)
for i in divisors:
    my_sum += i
if my_sum == x:
    print('True')
else:
    print('False')


#Timed exercise 2: write a program to reverse the sentence wordwise.
sentence=input('Please enter a sentence: ')
words=sentence.split(' ')
words_reverse= reversed(words)
sentence_reverse= ' '.join(words_reverse)
print(sentence_reverse)
