class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = [(-abs(arr[0] - x), 0)]
        for i in range(1, len(arr)):
            heappush(h, (-abs(arr[i] - x), -i))
            if len(h) > k:
                heappop(h)
        return sorted([arr[-i] for v, i in h])