class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            even_counts = defaultdict(int)
            odd_counts = defaultdict(int)
            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd_counts[nums[j]] += 1
                else:
                    even_counts[nums[j]] += 1
                if len(even_counts) == len(odd_counts):
                    ans = max(ans, j - i + 1)
        return ans