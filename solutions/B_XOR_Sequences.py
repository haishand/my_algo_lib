t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    # convert a to binary and reverse it
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]

    n = max(len(a_bin), len(b_bin))
    a_bin = a_bin.zfill(n)
    b_bin = b_bin.zfill(n)

    cnt = 0
    for i in range(n - 1, -1, -1):
        if a_bin[i] == b_bin[i]:
            cnt += 1
        else:
            break
    print(2**cnt)
