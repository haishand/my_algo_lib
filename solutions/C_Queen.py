import sys

from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def solve():
    n = int(input())
    childs = [[] for _ in range(n + 1)]
    c = [0] * (n + 1)
    root = -1
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        if a == -1:
            root = i
        else:
            childs[a].append(i)
        c[i] = b

    ans = []
    vis = [False] * (n + 1)

    @bootstrap
    def dfs(x):
        if vis[x]:
            yield None
        vis[x] = True
        all = 1
        for y in childs[x]:
            all &= c[y]
            yield dfs(y)
        if all and c[x] == 1:
            ans.append(x)
        yield None

    dfs(root)
    # sort ans
    ans.sort()
    if len(ans) == 0:
        print(-1)
    else:
        print(" ".join(map(str, ans)))


solve()
