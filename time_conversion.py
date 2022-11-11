#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM": # checks if it is AM
        if s[:2] == "12": 
            return "00"+s[2:-2] # if 12 it removes 12 and appends 00
        else:
            return s[:-2] # else it is printed without the suffix
    else:
        hr = int(s[:2]) # makes first two elements as integer
        if (hr < 12):
            hr += 12 # if it is less then 12 then 12 is added to it
        return str(hr) + s[2:-2] # it is reverted back to string and returned along with elements eliminating first two as well as the suffix
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
    
    print(s)
