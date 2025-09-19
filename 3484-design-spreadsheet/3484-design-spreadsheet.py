class Spreadsheet:

    def __init__(self, rows: int):
        self.ss = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.ss[cell] = value

    def resetCell(self, cell: str) -> None:
        self.ss[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")
        if x.isdigit() and y.isdigit():
            return int(x) + int(y)
        elif x.isdigit():
            return int(x) + self.ss[y]
        elif y.isdigit():
            return self.ss[x] + int(y)
        else:
            return self.ss[x] + self.ss[y]


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)