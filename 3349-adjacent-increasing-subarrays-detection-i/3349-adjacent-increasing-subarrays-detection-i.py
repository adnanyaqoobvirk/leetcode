class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        k2 = 2 * k
        n = len(nums)
        prev, curr = 0, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1

            if curr >= k2 or min(prev, curr) >= k:
                return True
        return False