class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        
        for idx, word in enumerate(words):
            for i in reversed(range(len(word))):
                suffix = word[i:] + '#'
                t = self.trie
                for c in suffix:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                
                for c in word:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                    t['$'] = idx

    def f(self, prefix: str, suffix: str) -> int:
        word = f"{suffix}#{prefix}"
        t = self.trie
        for c in word:
            if c not in t:
                return -1
            t = t[c]
        return t['$']

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)