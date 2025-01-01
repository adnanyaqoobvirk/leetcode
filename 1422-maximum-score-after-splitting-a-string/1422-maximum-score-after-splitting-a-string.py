class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_ones = 0
        for c in s:
            if c == "1":
                total_ones += 1
        
        ans = zeros = ones = 0
        for c in s:
            if c == "0":
                zeros += 1
            else:
                ones += 1
            ans = max(ans, zeros + total_ones - ones)
        return ans