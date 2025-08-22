class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        phrases = [p.split(" ") for p in phrases]
        pmap = defaultdict(list)
        for i, p in enumerate(phrases):
            pmap[p[0]].append((i, p))
        
        ans = set()
        for i, bp in enumerate(phrases):
            for j, ap in pmap[bp[-1]]:
                if i != j:
                    res = bp[::]
                    for k in range(1, len(ap)):
                        res.append(ap[k])
                    ans.add(" ".join(res))
        return sorted(ans)