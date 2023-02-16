#A deque is a double-ended queue. It can be used to add or remove elements from both ends.


#  Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

D = deque()

for _ in range(int(input())):
    oper, val, *args = input().split() + ['']
    eval(f'D.{oper} ({val})')
print(*D)
