class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        vmap = defaultdict(int)
        for i, num in enumerate(nums):
            vmap[-num] = i
        
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = nums[i] + nums[j]
                if k in vmap and i < vmap[k] and j < vmap[k]:
                    ans.add((nums[i], nums[j], -k))
        return ans