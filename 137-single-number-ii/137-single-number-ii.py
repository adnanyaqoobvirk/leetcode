class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for num in nums:
            if seen[num] == 2:
                del seen[num]
            else:
                seen[num] += 1
        return next(iter(seen))