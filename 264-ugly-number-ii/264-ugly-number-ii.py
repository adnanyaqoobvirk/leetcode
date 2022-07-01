from sortedcontainers import SortedSet

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        
        seen = SortedSet([1])
        for _ in range(n - 1):
            num = seen.pop(0)
            for f in factors:
                ugly = f * num
                if ugly not in seen:
                    seen.add(ugly)
        return seen.pop(0)