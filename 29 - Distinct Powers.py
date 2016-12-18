distinct_terms = []

for a in range(2, 101):
    for b in range(2, 101):
        power = a ** b

        if power not in distinct_terms:
            distinct_terms.append(power)

print(len(distinct_terms))