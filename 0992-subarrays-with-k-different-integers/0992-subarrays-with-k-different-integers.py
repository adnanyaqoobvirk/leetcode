class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(t):
            imap = {}
            count = lo = 0
            for hi in range(len(nums)):
                if nums[hi] not in imap:
                    imap[nums[hi]] = 1
                else:
                    imap[nums[hi]] += 1
                
                while lo <= hi and len(imap) > t:
                    imap[nums[lo]] -= 1
                    if imap[nums[lo]] == 0:
                        del imap[nums[lo]]
                    lo += 1
                
                count += hi - lo + 1
            return count
        return atMost(k) - atMost(k - 1)