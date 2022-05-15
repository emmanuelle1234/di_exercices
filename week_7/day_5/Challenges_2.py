# EXERCISE 1

for i in range(3):
    print(f'{(2-i) *" "}{i *"*"}*{i *"*"}')

print("\n")
for i in range(5):
    print((4 - i) * " ", (i+1) * "*")
print("\n")

for i in range(5):
    print((i+1) * "*", (5 - i) * " ")
for i in range(5):
    print(f'{i * " "}{(5 - i) * "*"}')

print("\n")

for i in range(10):
    print((i+1) * "*" if i < 5 else (i * " "), (5-i) * " " if i < 5 else ((5-i) * "*"))
    # don't understand why else action is not taken into account whereas the if condition does
print("\n")

# EXERCISE 2
#Instructions
# Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233] # create a list of numbers
for i in range(len(my_list) - 1): # create a loop (4 rounds from i = 0 to i = 5-1-1=3)
    minimum = i                   # the index of the round is defined as the minimum
    for j in range( i + 1, len(my_list)): # create a nested loop considering all the indexes which are strictly superior to the index of the nesting loop
        if(my_list[j] < my_list[minimum]): # if the figure corresponding to j is inferior to the one corresponding to i...
            minimum = j                     # j is now the index corresponding to the lowest figure among the two
            if(minimum != i):               # if i is not the index corresponding to the lowest figure among the two (not sure to understand why this if is required)
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # the list is reorganized so that the figure in the j (new min) position is before the other one
print(my_list)
"""i = 0 min (the figure) = 2
    j = 1 : 24 > 2 => nothing done min = 2
    j = 2 : 12 < 24 => 12 and 24 should be swapped
etc.
So the final output will be:
[2, 12, 24, 233, 354]
NB : to make the exercise a little bit more difficult, the index corresponding to the temporary min should be called with another name or nota named at all.
"""
# So the algo is ordering the list of numbers (ascending order)

