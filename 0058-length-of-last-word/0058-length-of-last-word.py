class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in reversed(range(len(s))):
            if s[i] == " ":
                if ans > 0:
                    break
            else:
                ans += 1
        return ans