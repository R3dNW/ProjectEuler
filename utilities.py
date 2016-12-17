import threading


def multiples_of(*nums, minimum=0, maximum=1000):
    results = []

    minimum = int(minimum)
    maximum = int(maximum)

    for i in range(minimum, maximum + 1):
        for num in nums:
            multiplier = i / num
            if multiplier == int(multiplier):
                results.append(i)
                break

    print(results)
    return results


def fibonacci(U0=1, U1=2, maxiumum=4000000):
    results = [U0, U1]

    while results[-1] <= maxiumum:
        results.append(results[-1] + results[-2])

    return results


primes_cache = [2]


def check_prime(value):
    if value in primes_cache:
        return True

    if value == 2:
        return True

    if value % 2 == 0:
        return False

    check_factors_up_to = int(value / 2) + 1
    last_factor_checked = 2

    for prime in primes_cache:
        if prime > check_factors_up_to:
            return True

        if value % prime == 0:
            return False

        last_factor_checked = prime

    for i in range((last_factor_checked - last_factor_checked % 2) + 1, check_factors_up_to + 1, 2):
        if i > check_factors_up_to:
            return True

        if value % i == 0:
            return False

    return True


def primes_below(minimum=0, maximum=1000):
    def sub(i):
        if check_prime(i):
            primes_cache.append(i)

    maximum = int(maximum)

    if maximum > primes_cache[-1]:
        for i in range((primes_cache[-1] - primes_cache[-1] % 2) + 1, maximum + 1, 2):
            t = threading.Thread(target=sub, args=[i])
            t.daemon = True
            t.start()

        if minimum <= 1:
            return primes_cache

    results = []

    for prime in primes_cache:
        if prime > maximum:
            break

        if minimum < prime:
            results.append(prime)

    return results


def find_nth_prime(n):
    def sub(i):
        if check_prime(i):
            primes_cache.append(i)

    if len(primes_cache) - 1 > n:
        return primes_cache[n - 1]

    last_value_checked = primes_cache[-1]
    while len(primes_cache) - 1 < n:
        t = threading.Thread(target=sub, args=[last_value_checked + 1])
        t.daemon = True
        t.start()

        last_value_checked += 1

    return primes_cache[n - 1]


def prime_factors_of(value):
    factors = []

    value = abs(value)

    while value != 1:
        for minimum in range(0, int(value / 2) + 1, 1000):
            primes = primes_below(minimum, minimum + 1000)

            for prime in primes:
                if value % prime == 0:
                    factors.append(prime)
                    value = int(value / prime)
                    break
            else:
                continue

            break
        else:
            factors.append(value)
            value = 1
            break

    return factors


def lcm(*args):
    all_prime_factors = {}

    for arg in args:
        factors_list = prime_factors_of(arg)

        collected_factors = {}

        for factor in factors_list:
            if factor in collected_factors.keys():
                collected_factors[factor] += 1
            else:
                collected_factors[factor] = 1

        for factor in collected_factors.keys():
            if factor in all_prime_factors:
                if collected_factors[factor] > all_prime_factors[factor]:
                    all_prime_factors[factor] = collected_factors[factor]
            else:
                all_prime_factors[factor] = collected_factors[factor]

    result = 1
    for factor in all_prime_factors.keys():
        result *= factor ** all_prime_factors[factor]

    return result


def sieve_primes_below(maximum=2000000):
    primes_list = list(range(2, maximum))

    index = 0
    prime = 0

    while prime ** 2 < maximum:
        prime = primes_list[index]

        new_primes_list = []

        for value in primes_list:
            if value % prime != 0 or value == prime:
                new_primes_list.append(value)

        primes_list = new_primes_list

        index += 1

    return primes_list
