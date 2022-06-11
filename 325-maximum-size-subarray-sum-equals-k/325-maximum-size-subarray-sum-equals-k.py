class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_map, prefix_arr, prefix = {0: -1}, [], 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix not in prefix_map:
                prefix_map[prefix] = i
            prefix_arr.append(prefix)
        
        max_len = 0
        for i, prefix in enumerate(prefix_arr):
            x = prefix - k
            if x in prefix_map:
                max_len = max(max_len, i - prefix_map[x])
        return max_len