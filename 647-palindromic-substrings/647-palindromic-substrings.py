class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        pmap = defaultdict(bool)
        pcount = 0
        
        for c in s:
            pmap[c] = True
            pcount += 1
            
        for i in range(1, n):
            if s[i - 1] == s[i]:
                pmap[f"{s[i - 1]}{s[i]}"] = True
                pcount += 1
        
        for i in range(3, n + 1):
            for j in range(n - i + 1):
                ss = s[j + 1:j + i - 1]
                if s[j] == s[j + i - 1] and pmap[ss]:
                    pmap[s[j:j + i]] = True
                    pcount += 1
                    
        return pcount