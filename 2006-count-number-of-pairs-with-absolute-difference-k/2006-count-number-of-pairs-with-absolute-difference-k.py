class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        ans = 0
        for i in range(k + 1, 201):
            ans += counts.get(i, 0) * counts.get(i - k, 0)
        return ans