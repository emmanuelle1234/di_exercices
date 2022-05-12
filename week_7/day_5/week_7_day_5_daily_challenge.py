# DAILY CHALLENGE DURING LESSON
""" INSTRUCTIONS
Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

# sequence = input('Please enter a sequence of words separated by a comma: ')
# step by step and inelegant

sequence = 'without,hello,bag,world'

sequence_list = sequence.split(",")
sorted_list = sorted(sequence_list)
sorted_sequence = ", ".join(sorted_list)
print(sorted_sequence)

# one liner without list comprehension
sorted_sequence = ", ".join(sorted(sequence.split(",")))
print(sorted_sequence)

# one liner with list comprehension
sorted_sequence = ", ".join(sorted(item for item in sequence.split(",")))
print(sorted_sequence)

# with list comprehension from a different sequence
sequence2 = 'without', 'hello', 'bag', 'world'
sorted_sequence2 = ", ".join(sorted(item for item in list(sequence2)))
print(sorted_sequence)
