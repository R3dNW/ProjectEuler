valid_products = []

for a in range(0, 1000):
    for b in range(0, 10000):
        product = a * b

        if product in valid_products:
            continue

        string = str(a) + str(b) + str(product)

        if len(string) > 9:
            break

        if len(string) < 9:
            continue

        if "1" in string and "2" in string and "3" in string and "4" in string and "5" in string and "6" in string and "7" in string and "8" in string and "9" in string:
            valid_products.append(product)

print(sum(valid_products))
