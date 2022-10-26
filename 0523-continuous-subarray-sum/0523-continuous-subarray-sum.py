class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: 0}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            r = total % k
            if r not in seen:
                seen[r] = i + 1
            elif seen[r] < i:
                return True
        return False