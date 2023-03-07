class WordDictionary:

    def __init__(self):
        self.t = {}

    def addWord(self, word: str) -> None:
        t = self.t
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["#"] = word

    def search(self, word: str) -> bool:
        def find(j, t):
            for i in range(j, n):
                if word[i] == '.':
                    for c in t:
                        if c != '#' and find(i + 1, t[c]):
                            return True
                    return False
                elif word[i] not in t:
                    return False
                t = t[word[i]]
            return '#' in t
        n = len(word)
        return find(0, self.t)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)