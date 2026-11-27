class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        chars = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])

            if r - l + 1 == k:
                count += 1
                chars.remove(s[l])
                l += 1
        return count
