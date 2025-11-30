class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = 0
        for num in nums:
            total = (total + num) % p

        if total == 0:
            return 0

        indices = {0: -1}
        curr_total = 0
        min_arr_length = len(nums)
        for i, num in enumerate(nums):
            curr_total = (curr_total + num) % p
            r = (curr_total - total + p) % p
            if r in indices:
                min_arr_length = min(min_arr_length, i - indices[r])
            indices[curr_total] = i
        return min_arr_length if min_arr_length != len(nums) else -1