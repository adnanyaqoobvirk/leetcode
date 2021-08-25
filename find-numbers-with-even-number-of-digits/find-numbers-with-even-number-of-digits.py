class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if int(math.log10(num)) & 1:
                count += 1
        return count