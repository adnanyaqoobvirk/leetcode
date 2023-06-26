class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums, count = set(arr), 0
        for x in arr:
            if x + 1 in nums:
                count += 1
        return count