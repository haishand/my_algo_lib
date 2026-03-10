n, m, k = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
if n <= k:
    ans = n
else:
    a = []
    for i in range(n - 1):
        a.append(b[i + 1] - b[i] - 1)
    a.sort()
    ans += n
    for i in range(0, n - k):
        ans += a[i]
print(ans)
