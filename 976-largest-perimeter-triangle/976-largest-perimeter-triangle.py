class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in reversed(range(len(nums))):
            a, b, c = nums[i], nums[i - 1], nums[i - 2]
            if a + b <= c or a + c <= b or b + c <= a:
                continue

            return a + b + c
        return 0
            