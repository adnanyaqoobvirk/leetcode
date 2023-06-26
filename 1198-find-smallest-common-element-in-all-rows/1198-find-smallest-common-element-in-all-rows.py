class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat) - 1, len(mat[0])
        for num in mat[-1]:
            for i in range(m):
                pos = bisect_left(mat[i], num)
                if pos == n or mat[i][pos] != num:
                    break
            else:
                return num
        return -1