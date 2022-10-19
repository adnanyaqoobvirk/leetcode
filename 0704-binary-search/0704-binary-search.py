class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return -1
        else:
            return l