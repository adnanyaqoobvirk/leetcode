class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count(v):
            res, j = 0, len(nums) - 1
            for i in range(len(nums)):
                while j > i and nums[i] + nums[j] > v:
                    j -= 1
                if i <= j:
                    res += j - i
            return res
        
        nums.sort()
        return count(upper) - count(lower - 1)