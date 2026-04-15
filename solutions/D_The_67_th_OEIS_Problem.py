import math


def sieve():
    # 先估算上限：第 1000 个素数大约是 8000 左右
    limit = 110000
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # 把 i 的倍数全筛掉
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


is_prime = sieve()
primes = [i for i, ok in enumerate(is_prime) if ok]
# print(len(primes))
t = int(input())
for _ in range(t):
    n = int(input())
    ans = [1] * n

    k = 1
    i = 0
    while k < n:
        ans[k] *= primes[i]
        if k + 1 >= n:
            break
        ans[k + 1] *= primes[i]
        k += 1
        i += 1
    # print(ans)
    # g = []
    # for i in range(1, n):
    #     g.append(math.gcd(ans[i], ans[i - 1]))
    # print(g)
    print(" ".join(map(str, ans)))
