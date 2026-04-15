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


@bootstrap
def dfs0(d, node, par, dep, mdep, edges):
    if dep[node] != -1:
        yield True
    dep[node] = d
    mdep[node] = dep[node]
    for u in edges[node]:
        if u != par:
            yield dfs0(d + 1, u, node, dep, mdep, edges)
            mdep[node] = max(mdep[node], mdep[u])
    yield True


@bootstrap
def dfs2(node, dep, sub, cost, a, edges, vis):
    vis[node] = True
    sub[node] = 0
    cost[node] = 0
    for u in edges[node]:
        if not vis[u]:
            yield dfs2(u, dep, sub, cost, a, edges, vis)
            sub[node] += a[u] + sub[u]
            cost[node] += a[u] + cost[u] + sub[u]
    yield True


@bootstrap
def dfs3(node, par, dep, mdep, cost, add, a, edges):
    f, s = 0, 0
    for u in edges[node]:
        if u != par:
            if mdep[u] > f:
                s = f
                f = mdep[u]
            elif mdep[u] > s:
                s = mdep[u]

    for u in edges[node]:
        if u != par:
            yield dfs3(u, node, dep, mdep, cost, add, a, edges)
            if mdep[u] != f:
                add[node] = max(add[node], add[u], (f - dep[u] + 1) * (a[u] + sub[u]))
            else:
                add[node] = max(add[node], add[u], (s - dep[u] + 1) * (a[u] + sub[u]))

    yield True


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    edges = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[u - 1].append(v - 1)
        edges[v - 1].append(u - 1)

    # calc depths and max depths
    dep = [-1] * n
    mdep = [0] * n
    dfs0(0, 0, -1, dep, mdep, edges)
    # print("dep:", dep)

    # calc cost without operation
    vis = [False] * n
    sub, cost = [0] * n, [0] * n
    dfs2(0, dep, sub, cost, a, edges, vis)
    # print("cost:", cost)

    # find max cost with 1 operation
    vis = [False] * n
    add = [0] * n
    dfs3(0, 0, dep, mdep, cost, add, a, edges)
    # print("add:", add)

    for i in range(n):
        cost[i] += add[i]
    print(" ".join(map(str, cost)))
