#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

##Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    positiveCounter = 0
    negetiveCounter = 0
    zeroCounter = 0

    for i in range (len(arr)):
        if arr[i] > 0:
            positiveCounter += 1
        elif arr[i] < 0 :
            negetiveCounter +=1
        else:
            zeroCounter += 1

    print("%f"%(positiveCounter / len(arr)))
    print("%f"%(negetiveCounter / len(arr)))
    print("%f"%(zeroCounter / len(arr)))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

