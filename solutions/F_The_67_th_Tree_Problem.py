t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    n = x + y
    if x == 0:
        if y % 2 != 0:
            print("YES")
            for i in range(2, n + 1):
                print(1, i)
        else:
            print("NO")
    elif y == 0:
        if x == 0:
            print("YES")
        else:
            print("NO")
    elif x > y:
        print("NO")
    else:
        d = y - x
        mm = 2 * x + (d % 2)
        print("YES")
        for i in range(1, mm):
            print(i, i + 1)
        for i in range(mm + 1, n + 1):
            print(mm, i)
