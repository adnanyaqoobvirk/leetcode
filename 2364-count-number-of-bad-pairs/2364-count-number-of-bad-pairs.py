class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = (n - 1) * n // 2
        
        counts = defaultdict(int)
        for i in range(n):
            counts[i - nums[i]] += 1
        
        good_pairs = 0
        for v in counts.values():
            if v > 1:
                good_pairs += (v - 1) * v // 2
        
        return total_pairs - good_pairs