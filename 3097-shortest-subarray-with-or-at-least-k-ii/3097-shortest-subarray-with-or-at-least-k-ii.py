class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        MAX_BITS = 32
        freq = [0] * MAX_BITS
        ans = inf
        curr = l = 0
        for r in range(len(nums)):
            for i in range(MAX_BITS):
                mask = 1 << i
                if mask > nums[r]:
                    break
                if nums[r] & mask:
                    freq[i] += 1
                    curr |= mask
                
            while l <= r and curr >= k:
                ans = min(ans, r - l + 1)
                for i in range(MAX_BITS):
                    mask = 1 << i
                    if mask > nums[l]:
                        break
                    if nums[l] & mask:
                        freq[i] -= 1
                        if freq[i] == 0:
                            curr &= ~mask
                l += 1
        return -1 if ans == inf else ans