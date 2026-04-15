class BinaryTrie:
    def __init__(self, max_bits):
        self.max_bits = max_bits
        self.trie = [[0, 0]]
        self.size = 0

    def insert(self, num):
        curr = 0
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            if not self.trie[curr][bit]:
                self.trie.append([0, 0])
                self.size += 1
                self.trie[curr][bit] = self.size
            curr = self.trie[curr][bit]

    def query_max_xor(self, num):
        """返回 num 与 Trie 中已有数字异或的最大值"""
        if not self.trie:
            return 0
        max_xor = 0
        curr = 0
        for i in range(self.max_bits, -1, -1):
            bit = (num >> i) & 1
            if self.trie[curr][1 - bit]:
                bit = 1 - bit
            max_xor |= bit << i
            curr = self.trie[curr][bit]
        return max_xor


n = int(input())
x = [*map(int, input().split())]
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] ^ x[i - 1]

bt = BinaryTrie(max_bits=29)
ans = 0
bt.insert(pre[0])
for i in range(n + 1):
    ans = max(ans, pre[i] ^ bt.query_max_xor(pre[i]))
    bt.insert(pre[i])

print(ans)
