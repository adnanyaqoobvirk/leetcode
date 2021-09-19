class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = [0] * 201
        for num in nums:
            counts[num] += 1
        ans = 0
        for i in range(k + 1, 201):
            ans += counts[i] * counts[i - k]
        return ans