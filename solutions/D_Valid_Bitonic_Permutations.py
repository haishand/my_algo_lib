from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


# fast power
@bootstrap
def fast_pow(base, n, mod):
    if n == 0:
        yield 1
        return
    res = yield fast_pow(base * base % mod, n // 2, mod)
    res %= mod
    if n % 2 != 0:
        res *= base
    res %= mod
    yield res


MOD = 10**9 + 7
N = 100

fact = [1] * (N + 1)
for k in range(1, N + 1):
    fact[k] = fact[k - 1] * k % MOD
inv_fact = [1] * (N + 1)
inv_fact[N] = fast_pow(fact[N], MOD - 2, MOD)

for k in range(N - 1, -1, -1):
    inv_fact[k] = inv_fact[k + 1] * (k + 1) % MOD


def Comb(n, k):
    if n < k or k < 0:
        return 0
    res = fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    return res % MOD


t = int(input())
for _ in range(t):
    n, i, j, x, y = map(int, input().split())
    if x > y:
        i, j = n - j + 1, n - i + 1
        x, y = y, x

    ans = 0
    if y == n:
        if j != n:
            ans = Comb(x - 1, i - 1) * Comb(n - x - 1, j - i - 1) % MOD
    else:
        # k in [i+1, j-1]
        ans1 = 0
        for k in range(i + 1, j):
            ans1 += Comb(n - y - 1, j - k - 1)
            ans1 %= MOD
        ans += ans1 * Comb(x - 1, i - 1) % MOD * Comb(y - x - 1, n - j - (x - i)) % MOD
        ans %= MOD

        # k in [j+1, n-1]
        ans2 = 0
        for k in range(j + 1, n):
            ans2 += Comb(n - y - 1, k - j - 1)
            ans2 %= MOD
        ans += ans2 * Comb(x - 1, i - 1) % MOD * Comb(y - x - 1, j - i - 1) % MOD
        ans %= MOD
    print(ans)
