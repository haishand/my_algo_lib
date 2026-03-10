n, a, x, y = map(int, input().split())

memo = {0: 0.0}


def solve(v):
    if v in memo:
        return memo[v]

    res1 = solve(v // a) + x

    res2 = 6.0 * y
    for i in range(2, 7):
        res2 += solve(v // i)
    memo[v] = min(res1, res2 / 5)
    return memo[v]


print(f"{solve(n):.7f}")
