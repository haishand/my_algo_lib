t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ans = 1
    has = False
    for i in range(1, n):
        if s[i] == s[i - 1]:
            has = True
            continue
        ans += 1

    if has and s[0] != s[-1]:
        ans += 1
    print(ans)
