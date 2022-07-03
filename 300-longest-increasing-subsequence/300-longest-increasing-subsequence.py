class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ss = [nums[0]]
        for i in range(1, len(nums)):
            lo, hi = 0, len(ss)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if ss[mid] >= nums[i]:
                    hi = mid
                else:
                    lo = mid + 1
            if lo == len(ss):
                ss.append(nums[i])
            else:
                ss[lo] = nums[i]
        return len(ss)