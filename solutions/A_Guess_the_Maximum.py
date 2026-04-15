t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = max(a)
    for i in range(1, n):
        ans = min(ans, max(a[i], a[i - 1]))
    print(ans - 1)
