#Given an array of integers, where all elements but one occur twice, find the unique element.
n=int(input())
a=list(map(int,input().split()))
r=a[0]
for i in range(1,n):
    r=r^a[i]
print(r)