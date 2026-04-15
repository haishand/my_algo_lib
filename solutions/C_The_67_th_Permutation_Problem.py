t = int(input())
for _ in range(t):
    n = int(input())
    a = list(range(1, 3 * n + 1))
    ans = []
    i, j = 0, len(a) - 1
    while i <= j:
        ans.append(a[j])
        ans.append(a[j - 1])
        ans.append(a[i])
        i += 1
        j -= 2
    print(" ".join(map(str, ans)))
