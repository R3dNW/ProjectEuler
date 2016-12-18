import threading

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]


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


primes_cache = sieve_primes_below(100000)


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

    if value in [1, 0]:
        return None

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


def collected_prime_factors_of(value):
    value = abs(value)

    if value in [1, 0]:
        return None

    factors_list = prime_factors_of(value)

    collected_factors = {}

    for factor in factors_list:
        if factor in collected_factors.keys():
            collected_factors[factor] += 1
        else:
            collected_factors[factor] = 1

    return collected_factors


def all_factors_of(num):
    if num == 1:
        return [1]

    if num == 0:
        return [0]

    if num == -1:
        return [-1]

    prime_factorisation = prime_factors_of(num)

    factors = []

    if num < 0:
        factors.append(-1)

    for i in range(0, 2 ** len(prime_factorisation)):
        pattern = str(bin(i))[2:]

        product = 1

        for x in range(0, len(pattern), 1):
            if pattern[-x - 1] == "1":
                product *= prime_factorisation[-x - 1]

        if product not in factors:
            factors.append(product)

    return sorted(factors)


def sum_of_proper_divisors(n):
    factors = all_factors_of(n)

    factors.remove(n)

    return sum(factors)


def check_perfect(num):
    return num == sum_of_proper_divisors(num)


def check_abundant(num):
    return sum_of_proper_divisors(num) > num


def check_deficient(num):
    return sum_of_proper_divisors(num) < num


def lcm(*args):
    all_prime_factors = {}

    for arg in args:
        collected_factors = collected_prime_factors_of(arg)

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


triangle_number_cache = [1]


def nth_triangle_number(n):
    for i in range(len(triangle_number_cache) + 1, n + 1):
        triangle_number_cache.append(triangle_number_cache[-1] + i)

    return triangle_number_cache[n - 1]


collatz_cache = {}


def collatz_length(n):
    if n == 1:
        return 0

    if n in collatz_cache.keys():
        return collatz_cache[n]

    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1

    chain_length = 1 + collatz_length(n)

    if n not in collatz_cache:
        collatz_cache[n] = chain_length

    return chain_length


def sum_of_digits(num):
    string = str(num)

    sum = 0

    for digit in string:
        sum += int(digit)

    return sum
