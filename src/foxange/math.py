import math
from collections.abc import Iterable
from math import sqrt
from numbers import Complex
from warnings import deprecated


@deprecated('Use math.gcd() instead')
def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


@deprecated('Use math.lcm() instead')
def lcm(a: int, b: int) -> int:
    return math.lcm(a, b)


@deprecated('Use math.comb() instead')
def combination(n: int, k: int) -> int:
    try:
        return math.comb(n, k)
    except ValueError:
        return 0


@deprecated('Use number1**number2 instead')
def pow(number1: float, number2: float) -> float:
    return number1**number2


@deprecated('Use int(math.sqrt()) instead')
def isqrt(n: int) -> int:
    return int(math.sqrt(n))


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number % 2 == 0:
        return False

    return all(number % i != 0 for i in range(3, int(sqrt(number)), 2))


def is_composite_number(number: int) -> bool:
    if number <= 1:
        return False

    return any(number % i == 0 for i in range(2, number))


def radical_sign(number: int, inx: int = 2) -> float:
    return pow(number, (1 / inx))


def factor(number: int, key=lambda _: True, recur=False) -> list[int]:
    ans: list = []
    limit = int(radical_sign(number)) + 1
    for i in range(1, limit):
        if number % i == 0:
            if key(i):
                ans.append(i)
            j = number // i
            if (i != j and key(j)) or (recur and key(j)):
                ans.append(j)
    return ans


def prime_factors(n: int) -> list[int]:
    if n <= 1:
        return []
    factors = [] if n % 2 != 0 else [2]
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)
    return factors


def sum(*value) -> int:
    ans: int = 0
    for i in value:
        if isinstance(i, Complex):
            ans += i  # type: ignore
        elif isinstance(i, Iterable):
            ans += sum(i)
    return ans


def digit_separation(number: int) -> list[int]:
    return [int(digit) for digit in str(number)]


def is_perfect_number(number: int) -> bool:
    number2 = sum(factor(number))
    return number2 == 2 * number


def is_excess_number(number: int) -> bool:
    number2 = sum(factor(number))
    return number2 > 2 * number


def is_deficit(number: int) -> bool:
    number2 = sum(factor(number))
    return number2 < 2 * number


def _sum_factor_without_self(n):
    return sum(factor(n)[:-1])


def _sum_factor_without_1_and_self(n):
    return sum(factor(n)[1:-1]) - n - 1


def is_amicable_numbers(number1: int, number2: int) -> bool:
    temp_number1 = _sum_factor_without_self(number1)
    temp_number2 = _sum_factor_without_self(number2)
    return temp_number1 == number2 and temp_number2 == number1


def is_engagements_number(number1: int, number2: int) -> bool:
    return (
        _sum_factor_without_1_and_self(number1) == number2
        and _sum_factor_without_1_and_self(number2) == number1
    )


def is_smith_number(number: int) -> bool:
    if number <= 1 or is_prime(number):
        return False
    factors = prime_factors(number)
    sum_factors_digits = sum(digit_separation(f) for f in factors)
    sum_original_digits = sum(digit_separation(number))
    return sum_factors_digits == sum_original_digits


def is_niven_number(number: int) -> bool:
    return number % sum(digit_separation(number)) == 0


def is_moran_number(number: int) -> bool:
    if not is_niven_number(number):
        return False
    temp = number // sum(digit_separation(number))
    return is_prime(temp)


def is_self_power_number(number: int) -> bool:
    digits = digit_separation(number)
    size = len(digits)
    temp = 0
    for i in digits:
        temp += pow(i, size)
    return temp == number


def is_narcissus_number(number: int) -> bool:
    return len(str(number)) == 3 and is_self_power_number(number)


def is_palindrome_number(number: int) -> bool:
    temp = digit_separation(number)
    return temp == temp[::-1]


def is_reversible_prime(number: int) -> bool:
    if not is_prime(number):
        return False
    rev = int(str(number)[::-1])
    return rev != number and is_prime(rev)


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def reverse_int(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev


def bin_to_int(n: str) -> int:
    return int(n, 2)


def int_to_bin(n: int) -> str:
    return f'{n:b}'


def digits_count(n) -> int:
    return len(str(n))


if __name__ == '__main__':
    import math
    import time

    start = time.time()
    print("math's", math.pow(10, 34))
    end = time.time()
    print(end - start)
    start = 0
    end = 0
    start = time.time()
    print("foxange's", pow(10, 34))
    end = time.time()
    print(end - start)
