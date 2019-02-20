#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counts = []
    x = list(set(ar))
    for i in x:
        val = ar.count(i)
        counts.append(val)
    myInt = 2
    newList = [math.floor(x / myInt) for x in counts]
    res = sum(newList)
    return(res)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
