from string import ascii_lowercase

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for j in reversed(range(n)):
            i = min(26, k - j)
            ans.append(ascii_lowercase[i - 1])
            k -= i
        return "".join(reversed(ans))