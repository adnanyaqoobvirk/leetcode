class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        tups = [tuple(row) for row in matrix]
        tcount = defaultdict(int)
        for t in tups:
            tcount[t] += 1
        ans = 0
        for i in range(len(matrix)):
            it = tuple(0 if num == 1 else 1 for num in matrix[i])
            ans = max(ans, tcount[tups[i]] + tcount[it])
        return ans