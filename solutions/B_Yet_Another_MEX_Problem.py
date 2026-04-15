def mex(a):
    sa = set(a)
    res = 0
    while res in sa:
        res += 1
    return res


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(min(mex(a), k - 1))
