from string import ascii_lowercase

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a'] * n
        for j in reversed(range(n)):
            i = min(26, k - j)
            if i == 1:
                break
            ans[j - n] = ascii_lowercase[i - 1]
            k -= i
        return "".join(ans)