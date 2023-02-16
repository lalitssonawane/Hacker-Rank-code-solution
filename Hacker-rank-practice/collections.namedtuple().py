#collections.namedtuple()
#Basically, namedtuples are easy to create, lightweight object types.
#They turn tuples into convenient containers for simple tasks.
#With namedtuples, you don’t have to use integer indices for accessing members of a tuple.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))