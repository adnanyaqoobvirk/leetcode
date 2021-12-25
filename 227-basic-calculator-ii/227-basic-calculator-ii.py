class Solution:
    def calculate(self, s: str) -> int:
        digits = {str(i): i for i in range(10)}
        ans, curr_int, prev_op = [], 0, ''
        for c in s:
            if c == ' ':
                continue
                
            if c in digits:
                curr_int = curr_int * 10 + digits[c]
            else:
                if prev_op == '/':
                    ans[-1] = (-1 if ans[-1] < 0 else 1) * (abs(ans[-1]) // curr_int)
                elif prev_op == '*':
                    ans[-1] *= curr_int
                else:
                    ans.append(-curr_int if prev_op == '-' else curr_int)
                curr_int, prev_op = 0, c
                
        if prev_op == '/':
            ans[-1] = (-1 if ans[-1] < 0 else 1) * (abs(ans[-1]) // curr_int)
        elif prev_op == '*':
            ans[-1] *= curr_int
        else:
            ans.append(-curr_int if prev_op == '-' else curr_int)
            
        return sum(ans)