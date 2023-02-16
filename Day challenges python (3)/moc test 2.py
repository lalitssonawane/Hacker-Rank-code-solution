#!/bin/python3
#https://www.hackerrank.com/challenges/flipping-the-matrix/problem
import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.
def flippingMatrix(matrix):
    l=[]
    n=len(matrix[0])//2
    for x in range(n):
        for y in range(n):
            l.append(max(matrix[x][y],matrix[x][2*n-y-1],matrix[2*n-x-1][y],matrix[2*n-x-1][2*n-y-1]))
    return sum(l)