class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if n <= 1:
            return nums
        
        left_nums, right_nums = self.sortArray(nums[0: n // 2]), self.sortArray(nums[n // 2:])
        
        sorted_nums = []
        lp = rp = 0
        while lp < len(left_nums) and rp < len(right_nums):
            if left_nums[lp] <= right_nums[rp]:
                sorted_nums.append(left_nums[lp])
                lp += 1
            else:
                sorted_nums.append(right_nums[rp])
                rp += 1
        
        extended_nums, p = (left_nums, lp) if lp < len(left_nums) else (right_nums, rp)
        while p < len(extended_nums):
            sorted_nums.append(extended_nums[p])
            p += 1
        
        return sorted_nums