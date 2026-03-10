class DSU:
    """
    Disjoint Set Union (DSU) data structure implementation.
    This class provides methods for efficiently managing and merging disjoint sets of elements.
    Attributes:
        parent (list): A list where parent[i] is the parent of element i. If parent[i] == i, then i is a representative of its set.
        rank (list): A list that keeps track of the rank (or depth) of each set for union by rank optimization.
        size (list): A list that keeps track of the size of each set for union by size optimization.
    """

    def __init__(self, n):
        self.parent = list(
            range(n + 1)
        )  # makes parent[i] = i for all i, meaning each element is its own parent initially
        self.rank = [1] * (n + 1)
        self.size = [1] * (n + 1)

    """
    The find method implements path compression to optimize the find operation. It returns the representative (or root) of the set that element a belongs to. 
    If a is not the representative of its set, it recursively finds the representative and updates the parent of a to point directly to the representative.
    """

    def find(self, a):
        if a == self.parent[a]:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]

    """
    The unite method merges the sets containing elements a and b. It first finds the representatives of both sets. 
    If they are different, it merges the smaller rank set into the larger rank set to keep the tree flat. 
    It also updates the size of the resulting set and increments the rank if both sets have the same rank.
    """

    def unite(self, a, b):
        x = self.find(a)
        y = self.find(b)

        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
