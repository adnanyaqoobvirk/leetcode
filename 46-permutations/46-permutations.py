class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper() -> None:
            if len(perm) == n:
                ans.append(perm[:])
            else:
                for i in range(n):
                    if nums[i] not in perm:
                        perm.append(nums[i])
                        helper()
                        perm.pop()
        n, ans, perm = len(nums), [], [] 
        helper()
        return ans