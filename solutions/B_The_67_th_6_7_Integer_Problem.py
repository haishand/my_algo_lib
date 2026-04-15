t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(6):
        ans += -1 * a[i]
    ans += a[6]
    print(ans)
