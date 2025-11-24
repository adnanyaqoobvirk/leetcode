class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        result = []
        for num in nums:
            x = (x * 2 + num) % 5
            result.append(x == 0)
        return result