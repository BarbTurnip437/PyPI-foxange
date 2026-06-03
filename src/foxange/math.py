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


def is_composite(number: int) -> bool:
    if number <= 1:
        return False

    return any(number % i == 0 for i in range(2, number))


def root(number: int, inx: int = 2) -> float:
    return math.pow(number, (1 / inx))


def factors(number: int, recur=False) -> list[int]:
    limit = int(root(number)) + 1
    ans = [i for i in range(1, limit) if number % i == 0]
    ans.extend([j for i in ans if i != (j := number // i) or recur])
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


def deep_sum(*value) -> int:
    ans: int = 0
    for i in value:
        if isinstance(i, Complex):
            ans += i  # type: ignore
        elif isinstance(i, Iterable):
            ans += __builtins__.sum(i)
    return ans


def digit_separation(number: int) -> list[int]:
    return [int(digit) for digit in str(number)]


def is_perfect(number: int) -> bool:
    number2 = sum(factors(number))
    return number2 == 2 * number


def is_excess(number: int) -> bool:
    number2 = sum(factors(number))
    return number2 > 2 * number


def is_deficit(number: int) -> bool:
    number2 = sum(factors(number))
    return number2 < 2 * number


def _sum_factor_without_self(n):
    return sum(factors(n)) - n


def _sum_factor_without_1_and_self(n):
    return sum(factors(n)) - n - 1


def is_amicable_pair(number1: int, number2: int) -> bool:
    temp_number1 = _sum_factor_without_self(number1)
    temp_number2 = _sum_factor_without_self(number2)
    return temp_number1 == number2 and temp_number2 == number1


def is_betrothed_pair(number1: int, number2: int) -> bool:
    return (
        _sum_factor_without_1_and_self(number1) == number2
        and _sum_factor_without_1_and_self(number2) == number1
    )


def is_smith(number: int) -> bool:
    if number <= 1 or is_prime(number):
        return False
    factors = prime_factors(number)
    sum_factors_digits = sum(sum(digit_separation(f)) for f in factors)
    sum_original_digits = sum(digit_separation(number))
    return sum_factors_digits == sum_original_digits


def is_harshad(number: int) -> bool:
    return number % sum(digit_separation(number)) == 0


def is_moran(number: int) -> bool:
    if not is_harshad(number):
        return False
    temp = number // sum(digit_separation(number))
    return is_prime(temp)


def is_self_power(number: int) -> bool:
    digits = digit_separation(number)
    size = len(digits)

    return sum(digit**size for digit in digits) == number


def is_narcissistic(number: int) -> bool:
    return len(str(number)) == 3 and is_self_power(number)


def is_palindrome(number: int) -> bool:
    number_str = str(number)
    return number_str == number_str[::-1]


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
    return sign * int(str(abs(n))[::-1])


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
