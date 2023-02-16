#Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.


cube = lambda x: x ** 3
def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))