class TextEditor:

    def __init__(self):
        self.prefix = []
        self.suffix = []

    def addText(self, text: str) -> None:
        for c in text:
            self.prefix.append(c)
            
    def deleteText(self, k: int) -> int:
        deleted = 0
        for _ in range(k):
            if not self.prefix:
                break
            self.prefix.pop()
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if not self.prefix:
                break
            self.suffix.append(self.prefix.pop())
        return "".join(self.prefix[max(0, len(self.prefix) - 10):])
    
    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if not self.suffix:
                break
            self.prefix.append(self.suffix.pop())
        return "".join(self.prefix[max(0, len(self.prefix) - 10):])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)