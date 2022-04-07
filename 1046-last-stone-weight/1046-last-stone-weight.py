class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapify(stones)
        while len(stones) > 1:
            x, y = abs(heappop(stones)), abs(heappop(stones))
            if x != y:
                heappush(stones, -abs(x - y))
        return -stones[0] if stones else 0