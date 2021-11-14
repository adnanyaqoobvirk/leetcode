from sortedcontainers import SortedDict

class Node:
    def __init__(self, val: int = 0, prev: 'Node' = None, next: 'Node' = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

class MaxStack:

    def __init__(self):
        self.map = SortedDict()
        self.tail = Node(float('inf'))
        
    def push(self, x: int) -> None:
        self.tail.next = Node(x, self.tail)
        self.tail = self.tail.next
        self.map.setdefault(x, []).append(self.tail)

    def pop(self) -> int:
        v = self.tail.val
        l = self.map[v]
        l.pop()
        if not l:
            self.map.pop(v)
        self.tail, self.tail.next = self.tail.prev, None
        return v

    def top(self) -> int:
        return self.tail.val
    
    def peekMax(self) -> int:
        return self.map.peekitem()[1][-1].val
    
    def popMax(self) -> int:
        l = self.map.peekitem()[1]
        node = l[-1]
        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.prev.next, node.next, node.prev = node.next, None, None
        l.pop()
        if not l:
            self.map.popitem()
        return node.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()