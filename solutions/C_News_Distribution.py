import sys
import os

# 將 src 目錄加入 Python 搜尋路徑
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_structures.dsu import DSU  # 現在可以引用了


def solve():
    n, m = map(int, input().split())
    uf = DSU(n)
    for _ in range(m):
        a = list(map(int, input().split()))
        if a[0] == 0:
            continue
        x = a[1]
        for i in range(1, a[0] + 1):
            uf.unite(x, a[i])
    ans = []
    for i in range(n):
        ans.append(uf.size[uf.find(i + 1)])
    print(" ".join(map(str, ans)))


solve()
