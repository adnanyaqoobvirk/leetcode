class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper() -> None:
            if len(perm) == n:
                ans.append(perm[:])
            else:
                for i in range(n):
                    if nums[i] not in seen:
                        perm.append(nums[i])
                        seen.add(nums[i])
                        helper()
                        perm.pop()
                        seen.discard(nums[i])
        n, ans, perm, seen = len(nums), [], [], set()
        helper()
        return ans