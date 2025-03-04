class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        t = self.tree
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = True

    def search(self, word: str) -> bool:
        t = self.tree
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return '#' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.tree
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)