# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
        
    def next(self) -> int:
        if self.hasNext():
            ans = self.stack[-1][0][self.stack[-1][1]]
            self.stack[-1][1] += 1
            return ans
    
    def hasNext(self) -> bool:
        while self.stack:
            nl, pos = self.stack[-1]
            if pos >= len(nl):
                self.stack.pop()
                continue
            
            if nl[pos].isInteger():
                break
            else:
                self.stack[-1][1] = pos + 1
                self.stack.append([nl[pos].getList(), 0])
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())