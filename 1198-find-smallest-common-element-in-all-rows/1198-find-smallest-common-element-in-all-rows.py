class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        itr = iter(mat)
        s = set(next(itr))
        for row in itr:
            s &= set(row)
        return min(s, default=-1)