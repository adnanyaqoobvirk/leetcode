class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        h = nums[::]
        heapify(h)
        return [heappop(h) for _ in range(len(h))]