t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] == 0 and a[n - 1] == 0:
        print("Bob")
    else:
        print("Alice")
