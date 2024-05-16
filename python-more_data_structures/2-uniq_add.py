#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbrs = set()
    for i in my_list:
        unique_numbrs.add(i)
    return sum(unique_numbrs)
