class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat) - 1, len(mat[0])
        freq = defaultdict(int)
        for i in range(m):
            for j in range(n):
                freq[mat[i][j]] += 1
        for num in mat[-1]:
            if freq[num] == m:
                return num
        return -1