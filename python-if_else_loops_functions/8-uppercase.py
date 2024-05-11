#!/usr/bin/python3
def uppercase(str):
    res = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{}".format(res), end='')
    print()
