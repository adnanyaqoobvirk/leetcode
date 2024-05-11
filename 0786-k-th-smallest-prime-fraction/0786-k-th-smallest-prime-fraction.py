class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = [(arr[i] / arr[j], arr[i], arr[j]) for i in range(n) for j in range(i + 1, n)]
        heapify(h)
        
        ans = None
        for _ in range(k):
            ans = heappop(h)
        return [ans[1], ans[2]]