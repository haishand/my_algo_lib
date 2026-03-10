import math

MOD = 1000000007
n, k = map(int, input().split())

factor = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            factor[i].append(j)
            if i // j != j:
                factor[i].append(i // j)

dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(n + 1):
    dp[1][i] = 1
for i in range(2, k + 1):
    for j in range(1, n + 1):
        for x in factor[j]:
            dp[i][j] += dp[i - 1][x]
            dp[i][j] %= MOD

ans = 0
for j in range(1, n + 1):
    ans += dp[k][j]
    ans %= MOD
print(ans)
