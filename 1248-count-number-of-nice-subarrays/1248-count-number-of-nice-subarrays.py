class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(t):
            odds = count = lo = 0
            for hi in range(len(nums)):
                if nums[hi] & 1:
                    odds += 1
                while lo <= hi and odds > t:
                    if nums[lo] & 1:
                        odds -= 1
                    lo += 1
                count += hi - lo + 1
            return count
        return atMost(k) - atMost(k - 1)