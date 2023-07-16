class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        @cache
        def dp(bm: int) -> int:
            if bm == mask:
                return 0
            
            ans, bcount = 0, inf
            for i, p in enumerate(people):
                tbm = bm
                for s in p:
                    if s in rmap:
                        tbm |= (1 << rmap[s])
                if tbm != bm:
                    res = 1 << i | dp(tbm)
                    if res.bit_count() < bcount:
                        ans, bcount = res, res.bit_count()
            return ans
        
        rmap, mask = {s: i for i, s in enumerate(req_skills)}, 0
        for i in range(len(req_skills)):
            mask |= (1 << i)
        
        pmask = dp(0)
        return [i for i in range(len(people)) if pmask & (1 << i)]