class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        j = 0
        ans = 0
        for i, c in enumerate(chain(s, "1")):
            if c == "1":
                if i - j > 1:
                    ans += ones
                ones += 1
                j = i
        return ans