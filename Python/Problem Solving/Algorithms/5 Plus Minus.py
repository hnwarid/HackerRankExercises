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
    pos = 0
    neg = 0 
    nul = 0
    for i in range(len(arr)):
        if arr[i] > 0:
           pos += 1
        elif arr[i] < 0:
            neg += 1
        else: 
            nul += 1
    pos /= len(arr)
    neg /= len(arr)
    if nul > 0:
        nul /= len(arr)
    print(f"{pos:.6f} \n{neg:.6f} \n{nul:.6f}") 
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
