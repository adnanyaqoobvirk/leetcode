class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ranges, prev = [], lower - 1
        for curr in nums:
            if curr - prev > 1:
                ranges.append([prev + 1, curr - 1])
            prev = curr
        if upper - prev >= 1:
            ranges.append([prev + 1, upper])
        return ranges