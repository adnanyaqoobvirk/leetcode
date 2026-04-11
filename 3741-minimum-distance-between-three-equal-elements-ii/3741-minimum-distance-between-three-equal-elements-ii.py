class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        n = len(nums)
        
        for i in range(n):
            indices[nums[i]].append(i)

        ans = inf
        for ilist in indices.values():
            if len(ilist) < 3:
                continue

            for k in range(2, len(ilist)):
                ans = min(ans, 
                          abs(ilist[k - 2] - ilist[k - 1]) + 
                          abs(ilist[k - 1] - ilist[k]) + 
                          abs(ilist[k] - ilist[k - 2])
                         )
        return -1 if ans == inf else ans