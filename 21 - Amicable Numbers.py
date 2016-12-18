import utilities
import threading

amicable_nums = []


def check_a(a):
    if a in amicable_nums:
        return

    b = utilities.sum_of_proper_divisors(a)
    result = utilities.sum_of_proper_divisors(b)

    if a == result and a != b:
        amicable_nums.append(a)

        if b not in amicable_nums:
            amicable_nums.append(b)


for a in range(2, 10000):
    t = threading.Thread(target=check_a, args=[a])
    t.daemon = True
    t.start()

print(amicable_nums)
print(sum(amicable_nums))

