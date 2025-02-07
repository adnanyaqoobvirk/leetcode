class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ic = {}
        ci = {}
        ans = []
        for i, c in queries:
            if i in ic:
                oc = ic[i]
                ci[oc].remove(i)
                if not ci[oc]:
                    del ci[oc]
            ic[i] = c
            if c not in ci:
                ci[c] = set()
            ci[c].add(i)
            ans.append(len(ci))
        return ans