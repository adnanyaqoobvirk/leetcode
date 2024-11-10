class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        MAX_BITS = 32
        freq = [0] * MAX_BITS
        ans = inf
        curr = l = 0
        for r in range(len(nums)):
            num = nums[r]
            for i in range(MAX_BITS):
                if num <= 0:
                    break
                if num & 1:
                    freq[i] += 1
                    curr |= 1 << i
                num >>= 1
                
            while l <= r and curr >= k:
                ans = min(ans, r - l + 1)
                num = nums[l]
                for i in range(MAX_BITS):
                    if num <= 0:
                        break
                    if num & 1:
                        freq[i] -= 1
                        if freq[i] == 0:
                            curr &= ~(1 << i)
                    num >>= 1
                l += 1
        return -1 if ans == inf else ans
            