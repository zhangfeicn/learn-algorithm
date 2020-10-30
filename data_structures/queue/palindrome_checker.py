from queue_on_list import Deque

"""
A palindrome is a string that reads the same forward and backward
"""

_created = '2020-03-30'


def is_palindrome(expr: str) -> bool:
    """Return True if it's palindrome; False otherwise."""
    charDeque = Deque()
    for ch in expr:
        charDeque.add_rear(ch)    # add char to the rear

    while charDeque.size() > 1:
        # pop from front and rear, then compare
        firstChar = charDeque.remove_front()
        lastChar = charDeque.remove_rear()
        if firstChar != lastChar:
            return False
    else:
        return True


def _main():
    examples = ["panama", "civic", "solos"]
    print("Palindrome demonstration:\n")
    for example in examples:
        print(example, ":", is_palindrome(example))


if __name__ == "__main__":
    _main()
