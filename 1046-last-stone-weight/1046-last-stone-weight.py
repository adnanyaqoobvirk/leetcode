class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        
        while len(stones) > 1:
            heappush(stones, -abs(heappop(stones) - heappop(stones)))
        return -stones[0]