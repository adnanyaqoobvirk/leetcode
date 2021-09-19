class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        curr = 'a'
        for c in word:
            diff = abs(ord(c) - ord(curr))
            ans += min(diff, 26 - diff) + 1
            curr = c
        return ans