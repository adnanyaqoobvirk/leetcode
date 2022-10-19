class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(l: int, r: int) -> int:
            if l > r:
                return -inf
            
            if l == r:
                return nums[l]
            
            mid = (r + l) // 2
            
            lmx = 0
            curr = 0
            for i in reversed(range(l, mid)):
                curr += nums[i]
                lmx = max(lmx, curr)
            
            rmx = 0
            curr = 0
            for i in range(mid + 1, r + 1):
                curr += nums[i]
                rmx = max(rmx, curr)
            
            lmax = helper(l, mid - 1)
            rmax = helper(mid + 1, r)
            
            return max(
                lmax,
                rmax,
                lmx + nums[mid] + rmx
            )
        
        n = len(nums)
        return helper(0, n - 1)