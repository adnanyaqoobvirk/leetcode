class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in reversed(range(2, len(nums))):
            a, b, c = nums[i], nums[i - 1], nums[i - 2]
            if b + c > a:
                return a + b + c
        return 0