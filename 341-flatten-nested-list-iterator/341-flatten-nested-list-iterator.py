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
        self.gen = self._generator(nestedList)
        self.nxt = None
        
    def _generator(self, nl: [NestedInteger]) -> None:
        for node in nl:
            if node.isInteger():
                yield node.getInteger()
            else:
                yield from self._generator(node.getList())
        
    def next(self) -> int:
        ans = self.nxt
        self.nxt = None
        return ans
    
    def hasNext(self) -> bool:
        if not self.nxt:
            try:
                self.nxt = next(self.gen)
                return True
            except:
                return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())