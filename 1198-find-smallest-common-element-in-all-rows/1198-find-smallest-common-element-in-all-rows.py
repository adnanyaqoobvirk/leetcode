class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_sets = [set(mat[i]) for i in range(1, m)]
        for e in mat[0]:
            for rs in row_sets:
                if e not in rs:
                    break
            else:
                return e
        return -1