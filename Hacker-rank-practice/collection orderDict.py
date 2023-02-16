#collections.OrderedDict
#An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

order = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)