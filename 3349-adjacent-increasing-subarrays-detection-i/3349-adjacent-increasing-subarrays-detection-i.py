class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev, curr = 0, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
                
            if curr >= 2 * k:
                return True

            if min(prev, curr) >= k:
                return True
        return False