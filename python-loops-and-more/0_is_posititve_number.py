#!/usr/bin/python3
import random
random_num = random.randint(-10, 10)
status = ("")
if random_num < 0:
    status = ("is negative")
elif random_num == 0:
    status = ("is zero")
elif random_num > 0:
    status = ("is pozitive")
print (random_num, status)
