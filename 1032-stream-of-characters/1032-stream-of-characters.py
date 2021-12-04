class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.maxlen = 0
        self.stream = deque()
        
        for word in words:
            t = self.trie
            self.maxlen = max(self.maxlen, len(word))
            for c in reversed(word):
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = True

    def query(self, letter: str) -> bool:
        if self.maxlen == len(self.stream):
            self.stream.popleft()
            
        self.stream.append(letter)
        
        t = self.trie
        for c in reversed(self.stream):
            if c not in t:
                break
                
            t = t[c]
            if '#' in t:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)