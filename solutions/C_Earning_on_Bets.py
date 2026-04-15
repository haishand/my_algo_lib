t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))

    # gcd of all elements in k
    from math import gcd

    lcm = k[0]
    for i in range(1, n):
        lcm = lcm * k[i] // gcd(lcm, k[i])

    s = 0
    for i in range(n):
        s += lcm // k[i]
    if s >= lcm:
        print(-1)
    else:
        for i in range(n):
            print(lcm // k[i], end=" ")
        print()
