class Solution:
    def maxProduct(self, words: List[str]) -> int:
        CHAR_START = ord('a')
        n = len(words)
        
        masks = []
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1 << (ord(c) - CHAR_START))
            masks.append(mask)
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans