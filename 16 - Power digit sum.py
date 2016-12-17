value = 2 ** 1000

string = str(value)

sum = 0

for digit in string:
    sum += int(digit)

print(sum)