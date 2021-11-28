class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = 0
        equals = 0
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                equals += 1
        return [i for i in range(smaller, smaller + equals)]