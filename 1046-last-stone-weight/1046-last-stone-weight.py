class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            heappush(stones, -abs(heappop(stones) - heappop(stones)))
        return -stones[0]