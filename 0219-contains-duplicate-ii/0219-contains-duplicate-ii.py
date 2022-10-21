class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        counts = defaultdict(int)
        for i in range(min(len(nums), k + 1)):
            if counts[nums[i]] > 0:
                return True
            counts[nums[i]] += 1
        
        l, r = 0, k + 1
        while r < len(nums):
            counts[nums[l]] -= 1
            if counts[nums[r]] > 0:
                return True
            counts[nums[r]] += 1
            l += 1
            r += 1
        
        return False
        