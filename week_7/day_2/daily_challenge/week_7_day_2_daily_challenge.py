# DAILY CHALLENGE
"""
I don't understand where is the remote learning “Matrix” videos mentioned in the hint.
I don't understand according to which rules the matrix is expected to be input.
I am not sure whether the 7 and 3 numbers in the example have a signification (resp. number of additional rows, number of columns)
Perhaps is it because I never watched the Matrix film?
"""

import re

# in case the user was expected to input the matrix
"""def matrix_build():
    rows_number = int(input('Please enter the number of rows in the matrix: '))
    first_row = input('Please enter the characters in the first row of the matrix: ')
    first_row_list = [letter for letter in first_row]
    print(first_row_list)
    matrix = [first_row_list]
    columns_number = len(first_row_list)
    for _ in range(rows_number-1):
        row = input(f'Please enter the next row of the matrix using {columns_number} character (space is possible) : ')
        matrix.append([letter for letter in row])
    return matrix
matrix = matrix_build()
print(matrix)"""

# to avoid to input the matrix to test with the previous function in comment!
matrix = [['7', 'i', '3'], ['T', 's', 'i'], ['h', '%', 'x'], ['i', "", '#'], ['s', 'M', ""], ['$', 'a', ""],
          ['#', 't', '%'], ['^', 'r', '!']]

# to have a look at the matrix as it is shown in the instruction
def matrix_display(matrix):
    for i in matrix:
        print('\t'.join(map(str,i))) #reminder: map(str,i) converts all i of a row into a string

matrix_display(matrix)

# matrix transposition to "read" by column
matrix = list(zip(*matrix))
matrix_display(matrix)

# it's time to de-cypher
print(matrix)
matrix_string = str()
for tuple in matrix:
    for character in tuple:
        matrix_string += character
print(matrix_string)

# These regex are a nightmare even with regex101.com.
matrix_string_without_figures = re.sub(r'(\d)', '', matrix_string)
hidden_message= re.sub(r'([^\w]+)', ' ',matrix_string_without_figures)
print(hidden_message)


