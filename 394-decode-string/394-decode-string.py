class Solution:
    def __init__(self):
        self.digits = {str(i): i for i in range(10)}
        
    def decodeString(self, s: str) -> str:
        ans, r, bcount, ss = [], 0, 0, []
        for c in s:
            if bcount == 0:
                if c == '[':
                    bcount += 1
                elif c in self.digits:
                    r = r * 10 + self.digits[c]
                else:
                    ans.append(c)
            else:
                ss.append(c)
                
                if c == '[':
                    bcount += 1
                elif c == ']':
                    bcount -= 1
                
                if bcount == 0:
                    ss.pop()
            if c == ']' and bcount == 0:
                ans.append(r * self.decodeString("".join(ss)))
                ss, r = [], 0
        return "".join(ans)