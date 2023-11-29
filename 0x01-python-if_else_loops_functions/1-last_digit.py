#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigitnumber = abs(number) % 10
if number < 0:
    lastdigitnumber = -(lastdigitnumber)
string = "Last digit of {} is {}".format(number, lastdigitnumber)
if lastdigitnumber > 5:
    print(f"{string} and is greater than 5")
elif lastdigitnumber == 0:
    print(f"{string} and is 0")
elif lastdigitnumber < 6:
    print(f"{string} and is less than 6 and not 0")
