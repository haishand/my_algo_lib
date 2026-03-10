class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)  # Depth of each set
        self.size = [1] * (n + 1)  # Size of each set

    def find(self, a):
        if a == self.parent[a]:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])  # path compression optimization
            return self.parent[a]

    def unite(self, a, b):
        x = self.find(a)
        y = self.find(b)

        # it's same if x==y, so only check x!=y
        if x != y:
            if self.rank[x] < self.rank[y]:  # swap x and y to make code concisely
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
            if (
                self.rank[x] == self.rank[y]
            ):  # the depth plus 1for the same depth after unite
                self.rank[x] += 1


n, m = map(int, input().split())
dsu = DSU(n)
for _ in range(m):
    a, b = map(int, input().split())
    dsu.unite(a, b)

ans = 0
for i in range(1, n + 1):
    if dsu.find(i) == i:
        ans += dsu.size[i] * (dsu.size[i] - 1) // 2
print(ans - m)
