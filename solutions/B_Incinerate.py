"""
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))

    a = []
    for i in range(n):
        a.append((h[i], p[i]))
    a.sort(key=lambda x: (x[1], x[0]))

    total_damage = k
    damage = k
    for i in range(n):
        hh, pp = a[i][0], a[i][1]
        hh -= total_damage
        if hh <= 0:
            continue
        die = False
        while hh > 0 and damage > 0:
            damage -= pp
            if damage <= 0:
                die = True
                break
            hh -= damage
            total_damage += damage
        if die:
            break
    if total_damage >= max(h):
        print("YES")
    else:
        print("NO")
"""

import bisect

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))

    a = []
    for i in range(n):
        a.append((h[i], p[i]))
    a.sort(key=lambda x: x[0])

    min_p = [x[1] for x in a]
    for i in range(n - 1, 0, -1):
        min_p[i - 1] = min(min_p[i], a[i - 1][1])

    hh = [x[0] for x in a]
    # print("hh:", hh)
    # print("min_p:", min_p)
    damage = k
    total_damage = k
    while damage > 0:
        pos = bisect.bisect_right(hh, total_damage)
        if pos == n:
            break
        damage -= min_p[pos]
        total_damage += damage

    # print(total_damage)
    if total_damage >= max(h):
        print("YES")
    else:
        print("NO")
