class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)

        counts = defaultdict(int)
        goods = 0
        pairs = 0
        l = 0
        for r in range(n):
            counts[nums[r]] += 1
            if counts[nums[r]] > 1:
                pairs += counts[nums[r]] - 1
            
            while l < r and pairs >= k:
                goods += n - r
                if counts[nums[l]] > 1:
                    pairs -= counts[nums[l]] - 1
                counts[nums[l]] -= 1
                l += 1
            
        return goods