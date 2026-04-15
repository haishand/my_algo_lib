t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            ans = max(ans, a[i] ^ a[j])
    print(ans)
