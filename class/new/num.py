# coding: utf-8
from random import randint
n = randint(1,100)
while (True):
    g = int(input('猜猜看'))
    if g > n:
        print('太大')
    if g < n:
        print('太小')
    if g == n :
        print('中')
        break