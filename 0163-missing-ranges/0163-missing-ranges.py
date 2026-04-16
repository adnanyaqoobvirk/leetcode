class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        prev = lower - 1
        for curr in chain(nums, [upper + 1]):
            if curr - prev > 1:
                ans.append([prev + 1, curr - 1])
            prev = curr
        return ans