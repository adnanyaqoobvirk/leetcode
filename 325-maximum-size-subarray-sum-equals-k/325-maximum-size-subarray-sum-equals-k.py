class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_map, prefix, max_len = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            prefix += num
            
            x = prefix - k
            if x in prefix_map:
                max_len = max(max_len, i - prefix_map[x])
                
            if prefix not in prefix_map:
                prefix_map[prefix] = i
        return max_len