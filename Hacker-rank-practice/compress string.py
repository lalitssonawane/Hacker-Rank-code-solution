#In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

#You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
#For a better understanding of the problem, check the explanation.



from itertools import groupby

for key, group in groupby(input()): 
    key= int(key)
    count = len(list(group))
    print((count,key),end=" ")