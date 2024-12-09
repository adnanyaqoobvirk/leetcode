class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        psums = [0]
        for i in range(1, len(nums)):
            psums.append(psums[-1])
            if nums[i] & 1 and nums[i - 1] & 1:
                continue
            if not (nums[i] & 1) and not (nums[i - 1] & 1):
                continue
            psums[i] += 1
        ans = []
        for i, j in queries:
            count = psums[j] - psums[i] 
            if count == j - i:
                ans.append(True)
            else:
                ans.append(False)
        return ans
