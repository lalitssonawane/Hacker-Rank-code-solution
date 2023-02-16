#The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.





import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))