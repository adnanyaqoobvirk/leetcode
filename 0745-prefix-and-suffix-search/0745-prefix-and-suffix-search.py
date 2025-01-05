class WordFilter:

    def __init__(self, words: List[str]):
        self.pt = {"#": []}
        for i, word in enumerate(words):
            t = self.pt
            for c in word:
                if c not in t:
                    t[c] = {"#": []}
                t = t[c]
                t["#"].append(i)
        self.st = {"#": set()}
        for i, word in enumerate(words):
            t = self.st
            for c in reversed(word):
                if c not in t:
                    t[c] = {"#": set()}
                t = t[c]
                t["#"].add(i)

    def f(self, pref: str, suff: str) -> int:
        t1 = self.pt
        for c in pref:
            if c not in t1:
                return -1
            t1 = t1[c]
        t2 = self.st
        for c in reversed(suff):
            if c not in t2:
                return -1
            t2 = t2[c]
        for i in reversed(t1["#"]):
            if i in t2["#"]:
                return i
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)