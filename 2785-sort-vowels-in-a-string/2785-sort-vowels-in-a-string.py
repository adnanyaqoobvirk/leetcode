class Solution:
    def sortVowels(self, s: str) -> str:
        vlist = list("AEIOUaeiou")
        vset = set(vlist)
        
        vcounts = defaultdict(int)
        for c in s:
            if c in vset:
                vcounts[c] += 1
        
        ans = []
        vpos = 0
        for c in s:
            if c not in vset:
                ans.append(c)
            else:
                while vpos < 10 and vcounts[vlist[vpos]] <= 0:
                    vpos += 1
                ans.append(vlist[vpos])
                vcounts[vlist[vpos]] -= 1
        return "".join(ans)