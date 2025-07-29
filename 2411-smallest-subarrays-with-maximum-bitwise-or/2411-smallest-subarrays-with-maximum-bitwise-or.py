class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mor = 0
        minBitLen = [n] * 31
        ans = [1] * n
        for i in reversed(range(n)):
            mor |= nums[i]
            for j in range(31):
                if nums[i] & (1 << j):
                    minBitLen[j] = min(minBitLen[j], i)
                if mor & (1 << j):
                    ans[i] = max(ans[i], minBitLen[j] - i + 1)
        return ans
