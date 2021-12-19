class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i: int) -> Tuple[int, str]:
            ans, r = [], 0
            while i < n:
                c = s[i]
                if c == '[':
                    i, ss = helper(i + 1)
                    while r > 0:
                        ans.extend(ss)
                        r -= 1
                elif c == ']':
                    break
                elif c in digits:
                    r = r * 10 + digits[c]
                else:
                    ans.append(c)
                i += 1
            return i, ans
        digits, n = {str(i): i for i in range(10)}, len(s)
        return "".join(helper(0)[1])