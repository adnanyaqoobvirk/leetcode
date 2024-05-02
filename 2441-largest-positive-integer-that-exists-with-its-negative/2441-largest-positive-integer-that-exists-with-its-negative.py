class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for num in nums:
            if abs(num) > ans and -num in seen:
                ans = abs(num)
            seen.add(num)
        return -1 if ans == 0 else ans