from itertools import accumulate

MOD = 676767677

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    b = [*map(int, input().split())]
    cnt = [0] * m
    for i in range(n):
        cnt[b[i]] += 1
    presum = [0, *accumulate(cnt)]
    ans = 1
    for i in range(n):
        if b[i] > 0:
            tt = float("inf")
            for j in (i - 1, i + 1):
                if j not in range(n):
                    continue
                tt = min(tt, b[j])

            if tt == b[i] - 1:
                ans = (ans * presum[b[i]]) % MOD
            elif tt < b[i] - 1:
                ans = (ans * cnt[b[i] - 1]) % MOD
            else:
                ans = 0
                break
            ans %= MOD
    print(ans)
