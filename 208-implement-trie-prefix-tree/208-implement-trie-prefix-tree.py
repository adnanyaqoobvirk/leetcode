class Trie:
    
    def __init__(self):
        self.nodes = [{}, False]

    def insert(self, word: str) -> None:
        pos, curr = 0, self.nodes
        while pos < len(word):
            char = word[pos]
            if char not in curr[0]:
                curr[0][char] = [{}, False]
            curr = curr[0][char]
            pos += 1
        curr[1] = True

    def search(self, word: str, prefix = False) -> bool:
        pos, curr = 0, self.nodes
        while pos < len(word):
            char = word[pos]
            if char not in curr[0]:
                return False
            curr = curr[0][char]
            pos += 1
        return curr[1] or prefix
    
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)