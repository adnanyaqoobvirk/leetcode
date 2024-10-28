from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sl = SortedList()
        ans = []
        for num in reversed(nums):
            sl.add(num)
            ans.append(sl.bisect_left(num))
        return ans[::-1]