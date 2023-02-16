#Comparison Sorting
#Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since  represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF)..
n = int(input())
ar = list(map(int, input().split()))

tot = [0]*100

for j in range(0,n):
    temp = ar[j]
    tot[temp] += 1
print(*tot, sep =' ')