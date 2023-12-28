#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_d = {}
    for a in a_dictionary:
        n_d[a] = a_dictionary[a] * 2
    return n_d
