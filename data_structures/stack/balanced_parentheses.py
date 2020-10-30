"""
Balanced parentheses means that each opening symbol has a corresponding
closing symbol and the pairs of parentheses are properly nested.

Algorithm : Starting with an empty stack, process the parenthesis strings
from left to right.  If a symbol is an opening parenthesis, push it on
the stack as a signal that a corresponding closing symbol needs to appear
later. If a symbol is a closing parenthesis, pop the stack.
"""

from stack_on_list import Stack

_created = "2020-03-28"


def is_matched(expr: str) -> bool:
    """
    Return True if all delimiters are properly match; False otherwise

    expr: expression to be checked, eg: (12 + 12)*(23 + 45)
        Parentheses: ( and )
        Braces: { and }
        Brackets: [ and ]
    """
    open_parentheses = '([{'
    closed_parentheses = ')]}'
    s = Stack(len(expr))

    for c in expr:
        if c in open_parentheses:
            s.push(c)
        elif c in closed_parentheses:
            if s.is_empty():
                return False
            if open_parentheses.index(s.pop()) != closed_parentheses.index(c):
                return False

    return s.is_empty()


def _main():
    examples = [
        "((()))",
        "((())",
        "(12 + 12)*(23 + 45)",
        "[(1+2)*(3+4)]"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        print(example + ": " + str(is_matched(example)))


if __name__ == "__main__":
    _main()
