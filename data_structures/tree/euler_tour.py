_created = "2020-05-02"


class EulerTour:
    """Abstract base class for performing Euler tour of a tree"""
    def __init__(self, tree):
        """Prepare an Euler tour template for given tree"""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed"""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        p   Position of current node being visited
        d   depth of p in the tree
        path    list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)  # add new index to end of path before recursion
        for c in self._tree.children(p):
            # recur on child s subtree
            results.append(self._tour(c, d + 1, path))
            path[-1] += 1
        path.pop()
        return self._hook_postvisit(p, d, path, results)

    def _hook_previsit(self, p, d, path):
        return

    def _hook_postvisit(self, p, d, path, results):
        return None


class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree"""
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()
        self._hook_visit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d + 1, path)
            path.pop()
        return self._hook_postvisit(p, d, path, results)

    def _hook_visit(self, p, d, path):
        pass


class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j + 1) for j in path)  # labels are one-indexed
        print(2 * d * ' ' + label, p.element())


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(', ', end='')
        print(p.element(), end='')
        if not self.tree().is_leaf(p):
            print(' (', end='')

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(')', end='')


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)
