class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rset = set(mat[0])
        for i in range(1, len(mat)):
            nrset = set()
            for v in mat[i]:
                if v in rset:
                    nrset.add(v)
            rset = nrset
        return min(rset)