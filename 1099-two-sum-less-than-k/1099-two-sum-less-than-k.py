class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        max_total = -1
        for i in range(n):
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                if total < k:
                    max_total = max(max_total, total)
        return max_total