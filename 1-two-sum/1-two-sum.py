class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {num:i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            j = num_map.get(target - num, -1)
            if i != j and j > -1:
                return [i, j]