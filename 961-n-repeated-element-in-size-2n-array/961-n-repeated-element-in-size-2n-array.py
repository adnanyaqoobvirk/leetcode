class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 3):
            seen = set()
            for i in range(i + 4):
                if nums[i] in seen:
                    return nums[i]
                seen.add(nums[i])