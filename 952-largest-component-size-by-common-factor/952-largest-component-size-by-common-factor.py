class DisjoinSet:
    def __init__(self, n: int) -> None:
        self.nodes = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        
    def find(self, i: int) -> int:
        if self.nodes[i] != i:
            self.nodes[i] = self.find(self.nodes[i])
        return self.nodes[i]
    
    def union(self, x: int, y: int) -> int:
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return xp
        
        if self.size[xp] > self.size[yp]:
            xp, yp = yp, xp
        
        self.nodes[xp] = yp
        self.size[yp] += self.size[xp]
        return xp
    
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        ds = DisjoinSet(max(nums))
        for num in nums:
            for f in range(2, int(sqrt(num)) + 1):
                if num % f == 0:
                    ds.union(num, f)
                    ds.union(num, num // f)
        
        counts = defaultdict(int)
        for num in nums:
            counts[ds.find(num)] += 1
        return max(counts.values())