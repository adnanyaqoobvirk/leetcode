class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(p: list) -> None:
            if len(p) == n:
                ans.append(p[::])
            else:
                for num in nums:
                    if num not in p:
                        p.append(num)
                        backtrack(p)
                        p.pop()
        ans, n = [], len(nums)
        backtrack([])
        return ans