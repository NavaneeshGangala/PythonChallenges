#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    path = list(s)
    path_move = [0]
    x=0
    for i in path:
        if i == 'U':
            x=x+1
            path_move.append(x)
        else:
            x=x-1
            path_move.append(x)
    y=0
    for idx, val in enumerate(path_move[:-1]):
      if val==0:
          if path_move[idx+1]==-1:
              y=y+1
    

    #counts = path_move.count(0)
    return(y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    

    fptr.write(str(result) + '\n')

    fptr.close()
