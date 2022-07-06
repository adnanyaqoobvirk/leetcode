class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        
        combs = 0
        for i in range(n - 2):
            lo = i + 2
            for j in range(i + 1, n - 1):
                total = nums[i] + nums[j]
                
                hi = n
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if nums[mid] >= total:
                        hi = mid
                    else:
                        lo = lo + 1
                combs += max(0, lo - j - 1)
        return combs