#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def new_matrix(matrix):
    for row in matrix:
       for number in row:
        print(number, end=" ")
    print()

new_matrix(matrix)  
