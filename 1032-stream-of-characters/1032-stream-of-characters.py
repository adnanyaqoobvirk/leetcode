class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = []
        
        for word in words:
            t = self.trie
            for c in reversed(word):
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        t = self.trie
        for c in reversed(self.stream):
            if c not in t:
                break
                
            t = t[c]
            if '#' in t:
                return True
        return False