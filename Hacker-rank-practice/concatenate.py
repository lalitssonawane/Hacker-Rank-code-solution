#Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

import numpy as np
a, b, c = map(int,input().split())
arr1 = np.array([input().split() for _ in range(a)],int)
arr2 = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arr1, arr2), axis = 0))