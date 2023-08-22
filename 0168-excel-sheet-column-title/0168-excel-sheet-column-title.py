class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, d = divmod(columnNumber, 26)
            ans.append(chr(ord('A') + d))
        return "".join(reversed(ans))