class Node:
    def __init__(self, ch: str, prev: 'Node' = None, nxt: 'Node' = None) -> None:
        self.ch = ch
        self.prev = prev
        self.next = nxt
    
    def __repr__(self):
        ans, cursor = [], self
        while cursor:
            ans.append(cursor.ch)
            cursor = cursor.next
        return "".join(ans)
        
class TextEditor:

    def __init__(self):
        self.head = self.cursor = Node('#')
        
    def addText(self, text: str) -> None:
        for c in text:
            next_prev = self.cursor.next
            self.cursor.next = Node(c, self.cursor, self.cursor.next)
            self.cursor = self.cursor.next
            if next_prev:
                next_prev.prev = self.cursor

    def deleteText(self, k: int) -> int:
        deleted = 0
        for _ in range(k):
            if self.cursor.ch == '#':
                break
            prev, nxt = self.cursor.prev, self.cursor.next
            self.cursor.next = self.cursor.prev = None
            self.cursor = prev
            self.cursor.next = nxt
            if self.cursor.next:
                self.cursor.next.prev = self.cursor
            deleted += 1
        return deleted
        
    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if self.cursor.ch == '#':
                return ""
            self.cursor = self.cursor.prev
        ans, cursor = [], self.cursor
        for _ in range(10):
            if cursor.ch == '#':
                break
            ans.append(cursor.ch)
            cursor = cursor.prev
        return "".join(reversed(ans))

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if not self.cursor.next:
                break
            self.cursor = self.cursor.next
        ans, cursor = [], self.cursor
        for _ in range(10):
            if cursor.ch == '#':
                break
            ans.append(cursor.ch)
            cursor = cursor.prev
        return "".join(reversed(ans))


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)