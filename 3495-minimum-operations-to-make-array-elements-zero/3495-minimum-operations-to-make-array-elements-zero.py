class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def getOps(num: int) -> int:
            total = 0
            prev, curr, ops = 1, 4, 1
            while curr <= num:
                total += (curr - prev) * ops
                prev, curr = curr, curr * 4
                ops += 1
            total += (num - prev + 1) * ops
            return total

        ans = 0
        for l, r in queries:
            ans += ceil((getOps(r) - getOps(l - 1)) / 2)
        return ans