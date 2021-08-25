class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digits = 0
            while num > 0:
                num //= 10
                digits += 1
            if not (digits & 1):
                count += 1
        return count