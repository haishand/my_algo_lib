n = int(input())
a = list(map(int, input().split()))

b = [0] * (n + 1)
for i in range(n):
    b[a[i]] = i

ans = []
for i in range(n):
    if a[i] == i + 1:
        continue
    j = b[i + 1]
    a[i], a[j] = a[j], a[i]
    b[a[j]] = j
    ans.append((i + 1, j + 1))
print(len(ans))
print("\n".join(map(lambda x: " ".join(map(str, x)), ans)))
