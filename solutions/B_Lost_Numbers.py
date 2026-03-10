import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")


def solve():
    s = set([4, 8, 15, 16, 23, 42])
    print("? 1 2")
    sys.stdout.flush()
    x = int(input())
    print("? 2 3")
    sys.stdout.flush()
    y = int(input())

    a = list()
    for d in s:
        if (
            x % d == 0
            and y % d == 0
            and (x // d) != (y // d)
            and (x // d) != d
            and (y // d) != d
            and (x // d) in s
            and (y // d) in s
        ):
            a.append(x // d)
            a.append(d)
            a.append(y // d)
            break

    print("? 4 5")
    sys.stdout.flush()
    x = int(input())
    print("? 5 6")
    sys.stdout.flush()
    y = int(input())

    for d in s:
        if (
            x % d == 0
            and y % d == 0
            and (x // d) != (y // d)
            and (x // d) != (y // d)
            and (x // d) != d
            and (y // d) != d
            and (x // d) in s
            and (y // d) in s
        ):
            a.append(x // d)
            a.append(d)
            a.append(y // d)
            break
    print("! " + " ".join(map(str, a)))
    sys.stdout.flush()


solve()
