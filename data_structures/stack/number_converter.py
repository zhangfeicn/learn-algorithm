from stack_on_list import Stack

_created = "2020-03-28"


def converter(decNumber: int, base: int) -> str:
    """
    decimal number system
    octal number system
    hexadecimal number system
    """
    s = Stack(decNumber // base + 1)
    digits = '0123456789ABCDEF'

    while decNumber:
        s.push(decNumber % base)
        decNumber //= base

    results = ''
    while not s.is_empty():
        results += digits[s.pop()]

    return results


def _main():
    examples = [2, 8, 16, 32]
    bases = [2, 8, 16]
    print("Number converter demonstration:\n")
    for example in examples:
        for base in bases:
            print(example, " to ", base, ": ", converter(example, base))


if __name__ == "__main__":
    _main()
