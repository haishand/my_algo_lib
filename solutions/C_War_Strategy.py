t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if k - 1 > n - k:
        k = n - k + 1

    # 注意a, b从0开始，所以a<k-1，b<n-k而不是a<k,b<=n-k
    a, b = 0, 0
    while True:
        if a < k - 1 and (a + 1) + b + max(a + 1, b) - 1 <= m:
            a += 1
        if b < n - k and a + (b + 1) + max(a, b + 1) - 1 <= m:
            b += 1
        else:
            break
    print(a + b + 1)
