class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        count = len(set(pattern))
        return filter(
            lambda word: count == len(set(word)) == len(set(zip(word, pattern))),
            words
        )