class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if cnt != 3:
                    return nums[i - 1]
                else:
                    cnt = 0
            cnt += 1
        return nums[-1]