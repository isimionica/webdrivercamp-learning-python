#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
Even_Odd_Tuple = tuple(i % 2 == 0 for i in my_list)
print(Even_Odd_Tuple) 
