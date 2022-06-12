class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_idx_map, prefix_sums = defaultdict(lambda: -1), []
        prefix = max_score = j = 0
        for i, num in enumerate(nums):
            if num_idx_map[num] >= j:
                max_score = max(max_score, (prefix - prefix_sums[j - 1]) if j > 0 else prefix)
                j = num_idx_map[num] + 1
            prefix += num
            prefix_sums.append(prefix)
            num_idx_map[num] = i
        max_score = max(max_score, (prefix - prefix_sums[j - 1]) if j > 0 else prefix)
        return max_score