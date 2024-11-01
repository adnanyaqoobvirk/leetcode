class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = [s[0], s[1]]
        for i in range(2, len(s)):
            if ans[-1] == ans[-2] == s[i]:
                continue
            ans.append(s[i])
        return "".join(ans)