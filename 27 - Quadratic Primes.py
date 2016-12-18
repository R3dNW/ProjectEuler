import utilities

a_max = 0
b_max = 0
n_max = 0

for a in range(-999, 1000):
    for b in utilities.primes_below(0, 1001):
        for signed_b in [-b, b]:
            n = 0
            while utilities.is_prime(abs(n * n + a * n + signed_b)):
                n += 1

            if n > n_max:
                a_max = a
                b_max = signed_b
                n_max = n

print(a_max * b_max)
