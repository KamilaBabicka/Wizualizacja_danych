def fib(n):
    a = 0
    b = 1
    for x in range(n):
        a, b = b, a + b
        yield a

gen = fib(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
