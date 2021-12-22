class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            dcount = 0
            while num > 0:
                num, _ = divmod(num, 10)
                dcount += 1
            if not (dcount & 1):
                ans += 1
        return ans