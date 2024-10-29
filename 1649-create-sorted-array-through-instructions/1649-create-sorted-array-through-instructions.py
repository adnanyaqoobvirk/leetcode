from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def update(i):
            while i < n:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        minv, maxv = min(instructions), max(instructions)
        offset = minv - 1
        n = maxv - minv + 2
        bit = [0] * n

        cost = 0
        for num in instructions:
            num = num - offset
            cost += min(query(num - 1), query(n - 1) - query(num))
            update(num)
        return cost % (10**9 + 7)