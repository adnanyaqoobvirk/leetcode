class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recurse(subset: List[int], pos: int) -> None:
            if pos == len(nums):
                xor = 0
                for num in subset:
                    xor ^= num
                output.append(xor)
            else:
                recurse(subset, pos + 1)
                subset.append(nums[pos])
                recurse(subset, pos + 1)
        output = []
        recurse([], 0)
        return sum(output)