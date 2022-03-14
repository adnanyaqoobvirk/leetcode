class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i: int) -> Tuple[int, str]:
            ans, k = [], 0
            while i < n:
                if s[i] == '[':
                    i, ss = helper(i + 1)
                    ans.extend(ss * k)
                    k = 0
                elif s[i] == ']':
                    break
                elif s[i] in digits:
                    k = k * 10 + digits[s[i]]
                else:
                    ans.append(s[i])
                i += 1
            return i, ans
        n, digits = len(s), {c: int(c) for c in "0123456789"}
        return "".join(helper(0)[1])