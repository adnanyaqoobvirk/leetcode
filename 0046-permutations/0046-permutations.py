class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm: List[int]) -> None:
            if len(perm) == n:
                ans.append(perm[::])
            else:
                for num in nums:
                    if num not in perm:
                        perm.append(num)
                        backtrack(perm)
                        perm.pop()
        ans = []
        n = len(nums)
        backtrack([])
        return ans