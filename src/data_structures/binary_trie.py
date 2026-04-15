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
        self.trie = [[0, 0]]
        self.size = 0

    @bootstrap
    def _insert(self, node, mbits, num):
        if mbits < 0:
            yield None
            return
        bit = (num >> mbits) & 1
        if not self.trie[node][bit]:
            self.trie.append([0, 0])
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


bt = BinaryTrie(max_bits=10)
# bt.insert(123)
# bt.insert(243)
# bt.insert(10)
# print(bt.trie)
n = bt.query_max_xor(20)
print(n)
