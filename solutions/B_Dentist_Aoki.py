n, q = map(int, input().split())
t = list(map(int, input().split()))

cnt = [0] * (n + 1)
for i in range(q):
    cnt[t[i]] += 1

ans = n
for i in range(n + 1):
    if cnt[i] % 2 == 1:
        ans -= 1
print(ans)
