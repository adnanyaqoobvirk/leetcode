class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prev = nums[0] - 1
        for num in nums:
            diff = num - prev - 1
            if k - diff <= 0:
                break
            k -= diff
            prev = num
        return prev + k