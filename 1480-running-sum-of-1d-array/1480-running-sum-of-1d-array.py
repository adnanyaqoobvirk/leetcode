class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans, rsum = [], 0
        for num in nums:
            rsum += num
            ans.append(rsum)
        return ans