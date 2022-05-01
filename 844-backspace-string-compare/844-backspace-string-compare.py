class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        for c in s:
            if c == '#':
                if sstack:
                    sstack.pop()
            else:
                sstack.append(c)
        
        tstack = []
        for c in t:
            if c == '#':
                if tstack:
                    tstack.pop()
            else:
                tstack.append(c)
        
        if len(sstack) != len(tstack):
            return False
        
        for i in range(len(sstack)):
            if sstack[i] != tstack[i]:
                return False
            
        return True