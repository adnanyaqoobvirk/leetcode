class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        k = sum(nums) - x
        
        if k == 0:
            return len(nums)
        
        prefix_map, prefix, max_len = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            prefix += num
            
            if prefix not in prefix_map:
                prefix_map[prefix] = i
            
            y = prefix - k
            if y in prefix_map:
                max_len = max(max_len, i - prefix_map[y])
        
        return len(nums) - max_len if max_len != 0 else -1