import utilities

seq = utilities.fibonacci_up_to_digits(1, 1, 1000)

for n in range(len(seq) - 1, -1, -1):
    if len(str(seq[n])) < 1000:
        print(n + 2)
        break
