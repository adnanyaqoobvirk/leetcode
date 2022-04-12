class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heappushpop(nums, nums[0] + 1)
        
        MOD, ans = 10**9 + 7, 1
        for num in nums:
            ans *= num
            if ans > MOD:
                ans %= MOD
        return ans % MOD