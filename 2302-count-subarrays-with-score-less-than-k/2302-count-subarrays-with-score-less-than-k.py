class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = total = ss_count = 0
        for right in range(len(nums)):
            total += nums[right]
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            ss_count += right - left + 1
        return ss_count