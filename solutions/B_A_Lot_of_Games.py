from pprint import pprint
from re import A


class Trie_scheme:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]


class Trie_cpp:
    def __init__(self) -> None:
        self.trie = [{}]

    def insert(self, word):
        curr = 0
        for c in word:
            if c not in self.trie[curr]:
                self.trie[curr][c] = len(self.trie)
                self.trie.append({})
            curr = self.trie[curr][c]


n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(input().strip())
print(words)
t = Trie()
for w in words:
    t.insert(w)
pprint(t.root)
pprint(t.root["a"])
