class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)
        ans = []
        j = 0
        for i, c in enumerate(s):
            if j < n and i == spaces[j]:
                ans.append(" ")
                j += 1
            ans.append(c)
        return "".join(ans)