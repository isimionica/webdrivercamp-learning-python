#!/usr/bin/python3
def fizz_buzz():
   for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz" , end = " ")
        elif x % 3 == 0:
            print('fizz', end = " ")
        elif x % 5 == 0:
            print('buzz', end = " ")
        else:
            print (x, end = " ") 
            
fizz_buzz()   
