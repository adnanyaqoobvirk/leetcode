class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            nrow = [1]
            for i in range(len(row) - 1):
                nrow.append(row[i] + row[i + 1])
            nrow.append(1)
            row = nrow
        return row
            