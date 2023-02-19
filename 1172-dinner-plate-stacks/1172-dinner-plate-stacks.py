class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.heap = [0]
        self.stacks = [[]]

    def push(self, val: int) -> None:
        while self.heap and (
            self.heap[0] >= len(self.stacks) or len(self.stacks[self.heap[0]]) == self.cap
        ):
            heappop(self.heap)
        
        if not self.heap:
            self.stacks.append([])
            heappush(self.heap, len(self.stacks) - 1)
        
        self.stacks[self.heap[0]].append(val)

    def pop(self) -> int:
        while self.stacks and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        
        if not self.stacks:
            return -1
        
        heappush(self.heap, len(self.stacks) - 1)
        return self.stacks[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        
        heappush(self.heap, index)
        return self.stacks[index].pop()

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

