class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        s_bspace_cnt = 0
        t_bspace_cnt = 0
        j = n - 1
        i = m - 1
        while True:
            while i >= 0:
                if s[i] == "#":
                    s_bspace_cnt += 1
                elif s_bspace_cnt > 0:
                    s_bspace_cnt -= 1
                else:
                    break
                i -= 1

            while j >= 0:
                if t[j] == "#":
                    t_bspace_cnt += 1
                elif t_bspace_cnt > 0:
                    t_bspace_cnt -= 1
                else:
                    break
                j -= 1
            
            if i < 0 or j < 0:
                break
            
            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
        return i < 0 and j < 0