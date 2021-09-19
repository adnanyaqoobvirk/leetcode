class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = [0] * 101
        for num in nums:
            counts[num] += 1
        ans = 0
        for i in range(k + 1, 101):
            ans += counts[i] * counts[i - k]
        return ans