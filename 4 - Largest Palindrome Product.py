max_x = 0
max_y = 0
max_product = 0

for x in range(100, 1001, 1):
    for y in range(100, 1001, 1):
        if x * y < max_product:
            continue

        string_value = str(x * y)

        reversed_value = ""

        for char in reversed(string_value):
            reversed_value += char

        if string_value == reversed_value:
            max_x = x
            max_y = y
            max_product = x * y

print(str(max_x) + " * " + str(max_y) + " = " + str(max_x * max_y))
