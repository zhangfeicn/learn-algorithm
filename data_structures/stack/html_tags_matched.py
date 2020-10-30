"""
Algorithm : Starting with an empty stack, make a left-to-right pass through
the raw string, using index j to track our progress and the find method of
the str class to locate the < and > characters that define the tags.
Opening tags are pushed onto the stack, and matched against closing tags
as they are popped from the stack,
"""

from stack_on_list import Stack

_created = "2020-03-29"


def is_matched_html(raw: str) -> bool:
    """Return True if all HTML tags are properly match; False otherwise."""
    s = Stack(len(raw))
    j = raw.find('<')                  # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)       # find next '>' character
        if k == -1:                    # invalid tag
            return False
        tag = raw[j + 1:k]             # strip away '<' '>'
        if not tag.startswith('/'):    # this is opening tag
            s.push(tag)
        else:                          # this is closing tag
            if s.is_empty():
                return False           # nothing to match with
            if tag[1:] != s.pop():     # mismatched delimiter, starts with \
                return False
        j = raw.find('<', k + 1)       # find next '<' character (if any)
    return s.is_empty()


def _main():
    example = """
    <body>
    <center>
    <h1> The Little Boat </h1>
    </center>
    <p> The storm tossed the little
    boat like a cheap sneaker in an
    old washing machine. The three
    drunken fishermen were used to
    such treatment, of course, but
    not the tree salesman, who even as
    a stowaway now felt that he
    had overpaid for the voyage. </p>
    <ol>
    <li> Will the salesman die? </li>
    <li> What color is the boat? </li>
    <li> And what about Naomi? </li>
    </ol>
    </body>
    """
    print("HTML tags match demonstration:\n")
    print(example + ": " + str(is_matched_html(example)))


if __name__ == "__main__":
    _main()
