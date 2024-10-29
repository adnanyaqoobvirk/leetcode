class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count(v):
            res, i, j = 0, 0, len(nums) - 1
            while i < j:
                while i < j and nums[i] + nums[j] > v:
                    j -= 1
                res += j - i
                i += 1
            return res
        
        nums.sort()
        return count(upper) - count(lower - 1)