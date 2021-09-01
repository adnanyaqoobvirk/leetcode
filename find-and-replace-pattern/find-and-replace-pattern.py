class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            mapping = {}
            for i, c in enumerate(word):
                if mapping.setdefault(pattern[i], c) != c:
                    break
            else:
                if len(set(mapping.values())) == len(mapping.keys()):
                    res.append(word)
        return res