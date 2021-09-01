class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        pat_count = len(set(pattern))
        for word in words:
            if pat_count == len(set(word)):
                mapping = {}
                for i, c in enumerate(word):
                    if mapping.setdefault(pattern[i], c) != c:
                        break
                else:
                    res.append(word)
        return res