#itertools.product()

#This tool computes the cartesian product of input iterables.
#It is equivalent to nested for-loops.
#For example, product(A, B) returns the same as ((x,y) for x in A for y in B).





# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product 
a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))