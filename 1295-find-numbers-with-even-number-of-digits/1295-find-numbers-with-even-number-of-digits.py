class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if int(math.log10(num)) & 1: ans += 1
        return ans