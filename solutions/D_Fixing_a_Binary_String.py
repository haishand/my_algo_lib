t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    base = ("0" * k + "1" * k) * (n // (2 * k) + 2)
    S0 = base[:n]
    S1 = base[k : n + k]
    # print(S0, S1)

    def check(S):
        return S == S0 or S == S1

    def operate(p):
        S = s[p:] + s[:p][::-1]
        if check(S):
            print(p)
        else:
            print(-1)

    # 从右往左找相同字符的个数x。之所以从右往左找，因为操作只能是前面部分。
    x = 0
    for i in range(n - 1, -1, -1):
        if s[i] == s[-1]:
            x += 1
        else:
            break

    # print(x)
    if x > k:
        print(-1)
    elif x == k:
        p = n
        for i in range(n - k - 1, -1, -1):
            if s[i] == s[i + k]:
                p = i + 1
                break

        operate(p)
    else:
        # x<k，看前面有没有k-x个或2k-x个相同字符
        was = False
        i = 0
        while i < n:
            if s[i] != s[-1]:
                i += 1
                continue
            j = i
            while j + 1 < n and s[i] == s[j + 1]:
                j += 1
            if j - i + 1 + x == k:
                operate(j + 1)
                was = True
                break
            elif j - i + 1 + x - k == k:
                operate(i + k - x)
                was = True
                break
            i = j
            i += 1

        if not was:
            operate(n)
