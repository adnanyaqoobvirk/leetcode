class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        l = start
        r = start
        while True:
            if l >= 0:
                if nums[l] == target:
                    return start - l
                l -= 1
            
            if r < n:
                if nums[r] == target:
                    return r - start
                r += 1
        return -1