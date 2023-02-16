# One of the built-in functions of Python is divmod, which takes two arguments  and  and returns a tuple containing the quotient of  first and then the remainder .
# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
B = int(input())

print(A//B)
print(A%B)
print(divmod(A, B))