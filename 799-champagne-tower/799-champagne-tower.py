class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ans = [poured]
        for i in range(1, query_row + 1):
            row = []
            for j in range(i + 1):
                val = 0.0
                if j > 0 and ans[j - 1] > 1:
                    val += (ans[j - 1] - 1) / 2
                if j < i and ans[j] > 1:
                    val += (ans[j] - 1) / 2
                row.append(val)
            ans = row
        return min(1.0, ans[query_glass])