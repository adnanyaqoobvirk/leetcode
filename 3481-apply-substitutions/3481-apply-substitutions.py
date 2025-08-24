class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        def solve(k: str) -> str:
            if "%" not in kmap[k]:
                return kmap[k]
            
            res = []
            i = 0
            v = kmap[k]
            n = len(v)
            while i < n:
                if v[i] == "%":
                    res.append(solve(v[i + 1]))
                    i += 3
                else:
                    res.append(v[i])
                    i += 1
            kmap[k] = "".join(res)
            return kmap[k]

        kmap = {"#": text}
        for k, v in replacements:
            kmap[k] = v
            
        return solve("#")