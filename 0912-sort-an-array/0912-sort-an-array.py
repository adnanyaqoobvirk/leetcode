class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        counts = Counter(nums)
        ans = []
        for num in range(mn, mx + 1):
            for cnt in range(counts[num]):
                ans.append(num)
        return ans