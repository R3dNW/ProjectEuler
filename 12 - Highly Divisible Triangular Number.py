import utilities

i = 1000

while True:
    i += 1
    triangle = utilities.nth_triangle_number(i)

    collected_factors = utilities.collected_prime_factors_of(triangle)

    number_of_factors = 1

    for power in collected_factors.values():
        number_of_factors *= power + 1

    if number_of_factors > 500:
        print(triangle)
        break
