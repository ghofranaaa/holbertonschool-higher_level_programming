#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    args = argv[1:]
    argc = len(args)
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} {'argument' if argc == 1 else 'arguments'}:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
