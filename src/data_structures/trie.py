from pprint import pprint


class Trie:
    def __init__(self):
        self.root = {}
        self.can_win, self.can_lose = {}, {}

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["end"] = True

    def dfs(self, )

t = Trie()
t.insert("hello")
pprint(t.root)
