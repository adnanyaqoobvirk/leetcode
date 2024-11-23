class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        nbox = [["."] * m for _ in range(n)]
        j = m - 1
        for row in box:
            i = n - 1
            for k in reversed(range(n)):
                if row[k] == "#":
                    nbox[i][j] = "#"
                    i -= 1
                elif row[k] == "*":
                    i = k
                    nbox[i][j] = "*"
                    i -= 1
            j -= 1
        return nbox

            