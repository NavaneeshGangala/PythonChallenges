#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    countA = s.count('a')
    rem = n % len(s)
    Qef = n // len(s)
    Add = s[:rem].count('a')

    TotalA = (countA*Qef) + Add
    return(TotalA)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
