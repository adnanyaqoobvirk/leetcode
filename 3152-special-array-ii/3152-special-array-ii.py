class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        smap = {0: 0}
        sindex = 0
        for i in range(1, len(nums)):
            if nums[i - 1] & 1 == nums[i] & 1:
                sindex += 1
            smap[i] = sindex
        return [smap[start] == smap[end] for start, end in queries]