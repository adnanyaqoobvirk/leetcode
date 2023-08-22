class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber, d = divmod(columnNumber, 26)
            if d == 0:
                ans.append("Z")
                columnNumber -= 1
            else:
                ans.append(chr(ord('A') + d - 1))
        return "".join(reversed(ans))