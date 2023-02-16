#The zeros tool returns a new array with a given shape and type filled with 's.









import numpy as np
shape= tuple(map(int,input().split()))
print(np.zeros(shape,int), np.ones(shape,int), sep='\n')