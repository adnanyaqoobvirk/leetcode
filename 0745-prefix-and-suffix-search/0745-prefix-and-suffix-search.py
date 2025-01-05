class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {"#": set()}
        for i, word in enumerate(words):
            t = self.trie
            for c in word:
                if c not in t:
                    t[c] = {"#": set(), "$": []}
                t = t[c]
                t["#"].add(i)

            t = self.trie
            for c in reversed(word):
                if c not in t:
                    t[c] = {"#": set(), "$": []}
                t = t[c]
                t["$"].append(i)

    def f(self, pref: str, suff: str) -> int:
        t = self.trie
        for c in pref:
            if c not in t:
                return -1
            t = t[c]
        pwords = t["#"]

        t = self.trie
        for c in reversed(suff):
            if c not in t:
                return -1
            t = t[c]
        swords = t["$"]

        for i in reversed(swords):
            if i in pwords:
                return i
        return -1
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)