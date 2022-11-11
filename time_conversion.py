#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00"+s[:-2]
        else:
            return s[:-2]
    else:
        hr = int(s[:2])
        if (hr < 12):
            hr += 12
        return str(hr) + s[2:-2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
    
    print(s)
