class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        for num, count in Counter(nums).items():
            heappush(h, (count, num))
            if len(h) > k:
                heappop(h)
        return [num for _, num in h]