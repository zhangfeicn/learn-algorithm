"""
Greatest Common Divisor.

Reference:
1. https://brilliant.org/wiki/greatest-common-divisor/
2. https://mathworld.wolfram.com/GreatestCommonDivisor.html
"""

_created = '2020-03-28'


def gcd(a, b):
    """
    Calculate Greatest Common Divisor (GCD).
    >>> gcd(3, 5) = 1
    >>> gcd(12, 60) = 12
    >>> gcd(12, 90) = 6
    """
    return a if b == 0 else gcd(b, a % b)


def _main():
    """ Invoke Greatest Common Divisor """
    try:
        nums = input("Enter two integers seperated by comma(','):").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(f"gcd({num_1}, {num_2}) = {gcd(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError) as e:
        # multiple exceptions
        print("Wrong Input:", e)


if __name__ == "__main__":
    _main()
