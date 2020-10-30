"""
Determining all factors of a positive integer
"""

_created = "2020-04-13"


# generator that computes factors
def factors(n: int):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def _main():
    print("Factors of 100")
    for v in factors(100):
        print(v, end=' ')
    print("\n")
    print("Factors of 128")
    for v in factors(128):
        print(v, end=' ')


if __name__ == "__main__":
    _main()
