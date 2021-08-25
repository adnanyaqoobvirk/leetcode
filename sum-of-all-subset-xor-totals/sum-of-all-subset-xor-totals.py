class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @cache
        def recurse(xor: int, pos: int) -> None:
            if pos == len(nums):
                return xor
            else:
                return recurse(xor, pos + 1) + recurse(xor ^ nums[pos], pos + 1)
        return recurse(0, 0)