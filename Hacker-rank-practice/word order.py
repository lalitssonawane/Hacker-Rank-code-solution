#You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

N = int(input())
LIST = []

for i in range(N):
    LIST.append(input().strip())

COUNT = Counter(LIST)

print(len(COUNT))
print(*COUNT.values())