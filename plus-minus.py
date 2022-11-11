#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    neg = 0
    pos = 0
    zero = 0
    
    #traverse through the list
    for i in arr:
        if i < 0:
            neg += 1 #inc if negative
        if i > 0:
            pos += 1 #inc if positive
        if i == 0:
            zero += 1 #inc if zero
    
    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
