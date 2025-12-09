class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        counts = defaultdict(int)
        target_counts = [0] * n
        for i in range(n):
            target_counts[i] = counts[nums[i] * 2]
            counts[nums[i]] += 1
        
        counts = defaultdict(int)
        triplet_count = 0
        for i in reversed(range(n)):
            triplet_count += target_counts[i] * counts[nums[i] * 2]
            counts[nums[i]] += 1
        return triplet_count % MOD