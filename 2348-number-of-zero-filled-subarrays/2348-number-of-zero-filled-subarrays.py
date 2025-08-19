class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                count = 0
            ans += count
        return ans