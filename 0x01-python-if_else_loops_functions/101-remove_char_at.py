#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    number = 0
    for char in str:
        if number != n:
            new += str[number]
        number += 1
    return (new)
