class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-g for g in gifts]
        heapify([])
        for _ in range(k):
            gift = heappop(h)
            heappush(h, -floor(sqrt(-gift)))
        return -sum(h)