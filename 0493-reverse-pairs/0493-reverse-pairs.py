from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList(key=lambda x: -x)
        ans = 0
        for num in nums:
            i = sl.bisect_left(2 * num)
            ans += i
            sl.add(num)
        return ans