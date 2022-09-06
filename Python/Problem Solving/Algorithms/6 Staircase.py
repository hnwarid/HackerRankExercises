#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    stairs = []
    for i in range(1, n+1):
        stairs.append(" "*(n-i) + ("#"*i))
    
    print("\n".join(stairs))
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
