#itertools.combinations_with_replacement(iterable, r)
#This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

#Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

S, k = map(str, input().split())

S = sorted(S)
k = int(k)

for e in list(combinations_with_replacement(S, k)):
    print(*e, sep='')