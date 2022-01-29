class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = {}

    def search(self, word: str) -> bool:
        q = [self.trie]
        for c in word:
            nq = []
            if c == '.':
                for node in q:
                    for k, v in node.items():
                        nq.append(v)
            else:
                for node in q:
                    if c in node:
                        nq.append(node[c])
            if not nq: return False
            q = nq
        for node in q:
            if '#' in node:
                return True
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)