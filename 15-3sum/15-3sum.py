class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, dups = set(), set()
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i + 1, len(nums)):
                    comps = -nums[i] - nums[j]
                    if seen.get(comps, -1) == i:
                        ans.add(tuple(sorted([nums[i], nums[j], comps])))
                    seen[nums[j]] = i
        return ans