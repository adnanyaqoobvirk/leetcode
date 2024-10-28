from sortedcontainers import SortedSet

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedSet()
        ans = []
        for num in reversed(nums):
            sl.add(num)
            ans.append(sl.bisect_left(num))
        return ans[::-1]