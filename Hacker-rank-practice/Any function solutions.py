#This expression returns True if any element of the iterable is true.
#If the iterable is empty, it will return False.



_ = input()
n = input().split()
print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))