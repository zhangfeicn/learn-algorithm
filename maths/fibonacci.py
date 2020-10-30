"""
Fibonacci generator
f1 = 0
f2 = 1
f3 = f1 + f2
"""

_created = "2020-04-13"


def fibonacci():
    f1, f2 = 0, 1
    while True:
        yield f1
        # f3 = f1 + f2
        f1, f2 = f2, f1 + f2


def _main():
    print("Fibonacci before 1000")
    for f in fibonacci():
        if f > 1000:
            break
        else:
            print(f, end=' ')


if __name__ == "__main__":
    _main()
