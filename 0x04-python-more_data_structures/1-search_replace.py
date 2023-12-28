#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            nw_list.append(replace)
        else:
            nw_list.append(my_list[i])
    return nw_list
