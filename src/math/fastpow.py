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


MOD = 1e9 + 7


@bootstrap
def fast_pow(base, n, mod):
    if n == 0:
        yield 1
        return
    res = yield fast_pow(base * base % mod, n // 2, mod)
    res %= mod
    if n % 2 != 0:
        res = (res * base) % mod
    yield res


n = 100
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD

inv_fact = [1] * (n + 1)
inv_fact[n] = fast_pow(fact[n], MOD - 2, MOD)
for i in range(n - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD


def C(n, k):
    if k < 0 or n < k:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD


i = 6
j = 15
x = 8
y = 17
N = 20
ans = C(x - 1, i - 1) * C(y - x - 1, j - i - 1) % MOD
print(ans)
s = 0
for k in range(j + 1, n):
    s += C(N - y, k - j)
    s %= MOD
ans *= s
print(ans)
