#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbrs = set()
    sum = 0
    for i in my_list:
        if i not in unique_numbrs:
            sum += i
            unique_numbrs.add(i)
        return sum
