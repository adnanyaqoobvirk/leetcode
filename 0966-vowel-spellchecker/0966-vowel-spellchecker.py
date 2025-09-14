class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(list("aeiou"))
        wmap = {}
        for i, word in enumerate(wordlist):
            wmap[word] = i
            t1, t2 = [], []
            for j, c in enumerate(word):
                c  = c.lower()
                t1.append((j, c))
                if c not in vowels:
                    t2.append((j, c))
            t1, t2 = tuple(t1), tuple(t2)
            if t1 not in wmap:
                wmap[t1] = i
            if t2 not in wmap:
                wmap[t2] = i
        
        ans = []
        for q in queries:
            if q in wmap:
                ans.append(q)
                continue

            t1, t2 = [], []
            for j, c in enumerate(q):
                c = c.lower()
                t1.append((j, c))
                if c not in vowels:
                    t2.append((j, c))
            
            t1, t2 = tuple(t1), tuple(t2)
            if t1 in wmap:
                ans.append(wordlist[wmap[t1]])
                continue
            
            if t2 in wmap:
                ans.append(wordlist[wmap[t2]])
                continue
            
            ans.append("")
        return ans