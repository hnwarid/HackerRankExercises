#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_str = s[:8]
    hh, mm, ss = time_str.split(':')
        
    if 'AM' in s and hh == '12':
        hh = '00'
    
    if 'PM' in s and hh != '12':
        hh = int(hh) + 12
        
    return f'{hh}:{mm}:{ss}'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
