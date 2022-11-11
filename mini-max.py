#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    arr.sort() # sorting the list
    mini = sum(arr[0:4]) # slices and sums the first 4 elements that forms minimum
    maxi = sum(arr[1:5]) # slices and sums the last four elements that forms maximum
    
    print(f'{mini} {maxi}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
