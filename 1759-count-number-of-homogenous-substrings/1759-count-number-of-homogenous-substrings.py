class Solution:
    def countHomogenous(self, s: str) -> int:
        p = ""
        count = 0
        ans = 0
        for c in s:
            if c != p:
                count = 0
                p = c
                
            count += 1
            ans += count
        return ans % (10 ** 9 + 7)