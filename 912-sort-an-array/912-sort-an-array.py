class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        sorted_nums = []
        while nums:
            sorted_nums.append(heappop(nums))
        return sorted_nums