class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 0
        pc = ""
        res = 1
        for c in word:
            if pc == c:
                cnt += 1
            else:
                res += cnt
                cnt = 0
                pc = c
        return res + cnt