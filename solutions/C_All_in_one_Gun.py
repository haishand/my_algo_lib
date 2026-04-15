t = int(input())
for _ in range(t):
    n, h, k = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)

    if h % total == 0:
        ans = (h // total - 1) * k + (h // total) * n
    else:
        ans = (h // total) * k + (h // total) * n
        mx = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            mx[i] = max(a[i], mx[i + 1])

        mi = [0] * (n + 1)
        mi[0] = a[0]
        for i in range(1, n):
            mi[i] = min(a[i], mi[i - 1])

        s = (h // total) * total
        for i in range(n):
            ans += 1
            s += a[i]
            if s - mi[i] + mx[i + 1] >= h or s >= h:
                break

    print(ans)
