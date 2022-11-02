class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        counts = defaultdict(int)
        for row in mat:
            for col in row:
                counts[col] += 1
                if counts[col] == m:
                    return col
        return -1