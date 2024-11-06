class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def bit_count(num: int) -> int:
            count = 0
            while num > 0:
                count += 1
                num -= num & -num
            return count

        has_swaps = True
        while has_swaps:
            has_swaps = False
            for i in range(1, len(nums)):
                if bit_count(nums[i]) == bit_count(nums[i - 1]) and nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    has_swaps = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        
        return True