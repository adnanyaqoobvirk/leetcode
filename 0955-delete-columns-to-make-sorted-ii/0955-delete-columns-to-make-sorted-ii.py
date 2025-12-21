class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def isSorted(rows: List[str]) -> bool:
            for i in range(1, m):
                if rows[i] < rows[i - 1]:
                    return False
            return True

        deletions = 0
        m, n = len(strs), len(strs[0])
        modified_strs = [""] * m
        for c in range(n):
            new_modified_strs = []
            for i in range(m):
                new_modified_strs.append(modified_strs[i] + strs[i][c])
            
            if isSorted(new_modified_strs):
                modified_strs = new_modified_strs
            else:
                deletions += 1
        return deletions