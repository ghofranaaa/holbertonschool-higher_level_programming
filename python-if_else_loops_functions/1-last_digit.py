#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
i = abs(number) % 10
if number < 0:
    i = i * -1
if i > 5:
    print('Last digit of %d is %d and is greater than 5' % (number, i))
elif i == 0:
    print('Last digit of %d is %d and is 0' % (number, n))
else:
    print('Last digit of %d is %d and is less than 6 and not 0' % (number, i))
