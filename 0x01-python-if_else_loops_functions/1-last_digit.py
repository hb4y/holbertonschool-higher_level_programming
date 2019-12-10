#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if (number < 0):
    last *= -1

str1 = "Last digit of {:d} is {:d} and is ".format(number, last)

if (last > 5):
    print(str1 + "greater than 5")
elif (last == 0):
    print(str1 + "0")
else:
    print(str1 + "less than 6 and not 0")
