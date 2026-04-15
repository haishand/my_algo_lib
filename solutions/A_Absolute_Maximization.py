import copy, math

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ma, mi = a[0], a[0]
    for i in range(1, n):
        ma |= a[i]
        mi &= a[i]
    print(ma - mi)
