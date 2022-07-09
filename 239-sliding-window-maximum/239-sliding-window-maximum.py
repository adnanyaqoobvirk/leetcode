from sortedcontainers import SortedSet

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedSet()
        for i in range(k):
            sl.add((nums[i], i))
            
        ans = [sl[-1][0]]
        for i in range(k, len(nums)):
            sl.remove((nums[i - k], i - k))
            sl.add((nums[i], i))
            ans.append(sl[-1][0])
        return ans
        