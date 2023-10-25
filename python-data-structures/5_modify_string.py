#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""
new_str = ' '
for char in string:
        if char not in ('A', 'a'):  
            new_str += char
print(new_str)        
