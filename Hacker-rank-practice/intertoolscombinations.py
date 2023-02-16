#itertools.combinations(iterable, r)
#This tool returns the  length subsequences of elements from the input iterable.

#Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations
string, n = input().split()
for i in range(1,int(n)+1):
    data = ["".join(sorted(i)) for i in combinations(string,i)]
    data.sort()
    print("\n".join(data))