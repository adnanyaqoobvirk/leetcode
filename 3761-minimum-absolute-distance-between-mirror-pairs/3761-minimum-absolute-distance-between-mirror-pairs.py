class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def getMirror(num: int) -> int:
            mirror = 0
            while num > 0:
                num, d = divmod(num, 10)
                mirror = mirror * 10 + d
            return mirror
        
        n = len(nums)
        min_dist = inf
        indices = {}
        for i in reversed(range(n)):
            num = nums[i]
            mirror = getMirror(num)
            if mirror in indices:
                min_dist = min(min_dist, abs(i - indices[mirror]))
            indices[num] = i
        return -1 if min_dist == inf else min_dist