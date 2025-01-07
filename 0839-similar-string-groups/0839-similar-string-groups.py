class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ss = set(strs)
        ans = 0
        while ss:
            g = [ss.pop()]
            i = 0
            while i < len(g):
                matches = []
                for e in ss:
                    dcount = 0
                    for j in range(len(e)):
                        if e[j] != g[i][j]:
                            dcount += 1
                    if dcount == 2:
                        matches.append(e)
                for m in matches:
                    g.append(m)
                    ss.remove(m)
                i += 1
            ans += 1
        return ans
