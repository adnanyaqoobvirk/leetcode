class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        for num, count in Counter(nums).items():
            if len(h) < k:
                heappush(h, (count, num))
            else:
                heappushpop(h, (count, num))
        return [num for _, num in h]