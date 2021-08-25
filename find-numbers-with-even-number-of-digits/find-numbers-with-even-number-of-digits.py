class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if math.floor(math.log(num + 1, 10)) & 1:
                count += 1
        return count