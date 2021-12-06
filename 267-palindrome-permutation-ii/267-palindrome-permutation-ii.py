class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def backtrack() -> None:
            if len(comb) == len(ss):
                cs = "".join([c for i, c in comb.keys()])
                ans.add(cs + odd_char + cs[::-1])
            else:
                for t in enumerate(ss):
                    if t not in comb:
                        comb[t] = True
                        backtrack()
                        del comb[t]
        
        counts = Counter(s)
        if len([c for c, count in counts.items() if count & 1]) > 1:
            return []
        
        odd_char = "".join(c for c, count in counts.items() if count & 1)
        ss = []
        for c, count in counts.items():
            ss.extend([c] * (count // 2))
        comb = {}
        ans = set()
        backtrack()
        return ans