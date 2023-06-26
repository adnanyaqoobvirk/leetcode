class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        lookup = {c:i for i, c in enumerate(keyboard)}
        ans = pre = 0
        for c in word:
            cur = lookup[c]
            ans += abs(cur - pre)
            pre = cur
        return ans