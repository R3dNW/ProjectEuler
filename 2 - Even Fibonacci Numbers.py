import utilities

fib = utilities.fibonacci(1, 2, 4000000)

even_fib = []

for i in range(0, len(fib)):
    if fib[i] % 2 == 0:
        even_fib.append(fib[i])

print(sum(even_fib))