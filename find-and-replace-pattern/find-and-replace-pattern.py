class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            mapping = {}
            rmapping = {}
            for i, c in enumerate(word):
                if (
                    mapping.setdefault(pattern[i], c) != c 
                    or 
                    rmapping.setdefault(c, pattern[i]) != pattern[i]
                ):
                    break
            else:
                res.append(word)
        return res