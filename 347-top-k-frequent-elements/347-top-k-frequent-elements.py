class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = [(-count, num) for num, count in Counter(nums).items()]
        heapify(h)
        return [heappop(h)[1] for _ in range(k)]