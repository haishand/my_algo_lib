from collections import defaultdict
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


class BinaryTrie:
    def __init__(self, max_bits):
        self.max_bits = max_bits
        self.trie = [[0, 0] for _ in range(10**5 * max_bits)]
        self.count = [0] * (10**5 * max_bits)
        self.size = 0

    @bootstrap
    def _insert(self, node, mbits, num):
        if mbits < 0:
            yield None
            return
        self.count[node] += 1
        bit = (num >> mbits) & 1
        if not self.trie[node][bit]:
            self.size += 1
            self.trie[node][bit] = self.size
        yield self._insert(self.trie[node][bit], mbits - 1, num)
        yield None

    def insert(self, num):
        self._insert(0, self.max_bits, num)

    @bootstrap
    def _query(self, node, mbits, num):
        if mbits < 0:
            yield 0
            return
        bit = (num >> mbits) & 1
        target = bit
        max_xor = 0
        if self.trie[node][1 - bit]:
            target = 1 - bit
        ret = yield self._query(self.trie[node][target], mbits - 1, num)
        max_xor = ret | (target << mbits)
        yield max_xor

    def query_max_xor(self, num):
        """返回 num 与 Trie 中已有数字异或的最大值"""
        return self._query(0, self.max_bits, num)

    @bootstrap
    def _query_under(self, node, mbits, num, K):
        if mbits < 0:
            yield 0
            return
        bit_N = (num >> mbits) & 1
        bit_K = (K >> mbits) & 1
        ans = 0
        same = self.trie[node][bit_N]
        diff = self.trie[node][1 - bit_N]
        if bit_K == 1:
            if same:
                ans += self.count[same]
            if diff:
                ans += yield self._query_under(diff, mbits - 1, num, K)
        else:
            if same:
                ans += yield self._query_under(same, mbits - 1, num, K)

        yield ans

    def query_under(self, num, K):
        return self._query_under(0, self.max_bits, num, K)


t = int(input())
n, k = map(int, input().split())
a = [*map(int, input().split())]
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] ^ a[i - 1]
ans = 0
bt = BinaryTrie(20)
bt.insert(pre[0])
for i in range(1, n + 1):
    ans += bt.query_under(pre[i], k)
    bt.insert(pre[i])
print(ans)
