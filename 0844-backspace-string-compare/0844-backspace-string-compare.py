class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextChar(inputStr: str) -> str:
            bspace_cnt = 0
            for c in reversed(inputStr):
                if c == "#":
                    bspace_cnt += 1
                elif bspace_cnt > 0:
                    bspace_cnt -= 1
                else:
                    yield c

        s_iter, t_iter = nextChar(s), nextChar(t)
        while True:
            schar = next(s_iter, None)
            tchar = next(t_iter, None)
        
            if schar != tchar:
                return False
            
            if schar is None and tchar is None:
                return True