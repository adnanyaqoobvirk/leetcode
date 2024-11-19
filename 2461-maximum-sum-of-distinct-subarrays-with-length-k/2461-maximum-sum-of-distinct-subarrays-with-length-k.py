class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        w = {}
        total = 0
        for i in range(k):
            w[nums[i]] = w.get(nums[i], 0) + 1
            total += nums[i]

        ans = total if len(w) == k else 0
        for i in range(k, len(nums)):
            w[nums[i]] = w.get(nums[i], 0) + 1
            w[nums[i - k]] -= 1
            if w[nums[i - k]] == 0:
                del w[nums[i - k]]
            total += nums[i]
            total -= nums[i - k]

            if len(w) == k:
                ans = max(ans, total)
        return ans