from itertools import permutations


def apply_change(v, l, r):
    segment = v[l : r + 1]
    mx = max(segment)
    mn = min(segment)
    for i in range(l, r + 1):
        v[i] = mx - mn


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    if n >= 4:
        ans = n * max(a)
    elif n == 3:
        # ans = max(
        #     sum(a),
        #     3 * a[0],
        #     3 * a[2],
        #     3 * abs(a[2] - a[0]),
        #     3 * max(a[0], abs(a[2] - a[1])),
        #     3 * max(a[2], abs(a[1] - a[0])),
        # )
        ops = [(0, 1), (0, 1), (1, 2), (1, 2), (0, 2)]
        ans = sum(a)
        for perm in permutations(ops):
            ca = a.copy()
            for x, y in perm:
                ll = ca[x]
                rr = ca[y]
                for k in range(x, y + 1):
                    ca[k] = abs(ll - rr)
                ans = max(ans, sum(ca))

    elif n == 2:
        ans = max(sum(a), 2 * abs(a[1] - a[0]))
    print(ans)
