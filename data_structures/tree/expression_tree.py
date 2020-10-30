from linked_binary_tree import LinkedBinaryTree

_created = "2020-05-02"


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree"""

    def __init__(self, token: str, left=None, right=None):
        """
        In a single parameter form, token should be a leaf value and the
        expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator, left and
        right should be existing ExpressionTree instances that become the
        operands for the binary operator.
        """

        super().__init__()
        self.add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self.attach(self.root(), left, right)

    def __repr__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, results):
        if self.is_leaf(p):
            results.append(p.element())
        else:
            results.append('(')
            self._parenthesize_recur(self.left(p), results)
            results.append(p.element())
            self._parenthesize_recur(self.right(p), results)
            results.append(')')

    def evaluate(self):
        """Return the numeric result of the expression"""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p"""
        if self.is_leaf(p):
            return p.element()
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression"""
    stack = []
    for t in tokens:
        if t in '+-*x/':
            stack.append(t)
        elif t not in '()':
            stack.append(ExpressionTree(t))
        elif t == ')':
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.append(ExpressionTree(op, left, right))
    return stack.pop()
