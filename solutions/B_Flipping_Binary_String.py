t = int(input())


def print_ans(ans):
    print(len(ans))
    if len(ans) > 0:
        print(" ".join(map(str, ans)))


for _ in range(t):
    n = int(input())
    s = input().strip()
    ans0, ans1 = [], []
    for i in range(n):
        if s[i] == "0":
            ans0.append(i + 1)
        else:
            ans1.append(i + 1)
    if len(ans1) % 2 == 0 or (len(ans0) % 2 == 1):
        if s.count("0") == n:
            print(0)
        else:
            if len(ans0) % 2 == 1:
                print_ans(ans0)
            else:
                print_ans(ans1)
    else:
        print(-1)
