#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    for a in roman_string:
        if (a != 'I' and a != 'V' and a != 'X' and
                a != 'L' and a != 'C' and a != 'D' and a != 'M'):
            return 0

    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = []

    for b in range(len(roman_string) - 1, -1, -1):
        if b == len(roman_string) - 1:
            largestNum = d[roman_string[b]]
        if d[roman_string[b]] < largestNum:
            num.append(largestNum - d[roman_string[b]])
            num.remove(largestNum)
            largestNum = d[roman_string[b]]
        else:
            num.append(d[roman_string[b]])
            largestNum = d[roman_string[b]]

    return sum(num)
