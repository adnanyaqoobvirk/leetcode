class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = ans = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                zeros = 0
            ans += zeros
        return ans