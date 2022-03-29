class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        heapify(nums)
        prev = heappop(nums)
        while len(nums) > 0:
            curr = heappop(nums)
            if curr == prev:
                return curr
            prev = curr