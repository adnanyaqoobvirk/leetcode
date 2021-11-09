class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):
            ss = []
            for j in range(len(nums)):
                if i & (1 << j):
                    ss.append(nums[j])
            ans.append(ss)
        return ans