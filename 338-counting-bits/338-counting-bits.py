class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ones = 0
            while i > 0:
                ones += 1
                i &= (i - 1)
            ans.append(ones)
        return ans
            