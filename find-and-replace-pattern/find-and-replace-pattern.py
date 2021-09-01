class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pat_count = len(set(pattern))
        return [
            word 
            for word in words 
            if pat_count == len(set(word)) == len(set(zip(word, pattern)))
        ]