class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max_val = 0
        for j in range(n):
            for k in range(j + 1, n):
                ans = max(ans, (max_val - nums[j]) * nums[k])
            max_val = max(max_val, nums[j])
        return ans