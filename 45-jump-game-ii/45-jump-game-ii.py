class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        jumps = farthest = jump_end = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == jump_end:
                jumps += 1
                jump_end = farthest
        return jumps