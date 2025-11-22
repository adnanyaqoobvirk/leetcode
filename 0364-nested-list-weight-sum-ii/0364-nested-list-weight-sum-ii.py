# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def getMaxDepth(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 1
        for node in nestedList:
            if not node.isInteger():
                max_depth = max(max_depth, 1 + self.getMaxDepth(node.getList()))
        return max_depth

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = self.getMaxDepth(nestedList)

        result = 0
        stack = [(nestedList, 1)]
        while stack:
            nlist, depth = stack.pop()

            for node in nlist:
                if node.isInteger():
                    result += node.getInteger() * (max_depth - depth + 1)
                else:
                    stack.append((node.getList(), depth + 1))
        return result