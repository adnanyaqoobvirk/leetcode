class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm: List[int]) -> None:
            if len(perm) == n:
                ans.append(perm[::])
            else:
                for num in counts:
                    if counts[num] > 0:
                        counts[num] -= 1
                        perm.append(num)
                        backtrack(perm)
                        perm.pop()
                        counts[num] += 1
        n = len(nums)
        counts = Counter(nums)
        ans = []
        backtrack([])
        return ans