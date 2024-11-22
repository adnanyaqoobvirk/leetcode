class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        trie = {}
        for row in matrix:
            t = trie
            for i in range(len(row)):
                c = "T" if row[i] == row[0] else "F"
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = t.get("#", 0) + 1
            ans = max(ans, t["#"])
        return ans