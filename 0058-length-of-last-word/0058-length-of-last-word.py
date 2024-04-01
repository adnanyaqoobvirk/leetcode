class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for c in reversed(s):
            if c == " ":
                if ans > 0:
                    break
            else:
                ans += 1
        return ans