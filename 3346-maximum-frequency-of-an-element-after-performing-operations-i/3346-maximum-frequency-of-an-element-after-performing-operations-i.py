class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        n = len(nums)
        counts = defaultdict(int)
        l = r = 0
        ans = 1
        for center in range(nums[0], nums[-1] + 1):
            while r < n and center + k >= nums[r]:
                counts[nums[r]] += 1
                r += 1
            while l < r and center - k > nums[l]:
                counts[nums[l]] -= 1
                l += 1
            ans = max(ans, min(counts[center] + numOperations, r - l))
        return ans