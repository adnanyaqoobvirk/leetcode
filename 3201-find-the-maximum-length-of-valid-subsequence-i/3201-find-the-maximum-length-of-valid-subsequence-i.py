class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evenCount = 0 if nums[0] & 1 else 1
        oddCount = 1 if nums[0] & 1 else 0
        pairCount = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] & 1:
                oddCount += 1
            else:
                evenCount += 1
            if (prev & 1 and not (nums[i] & 1)) or (not (prev & 1) and nums[i] & 1):
                pairCount += 1
                prev = nums[i]
        return max(evenCount, oddCount, pairCount)
