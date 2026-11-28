class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        ans = -1
        for num, count in Counter(nums).items():
            if count == 1 and num > ans:
                ans = num
        return ans
                