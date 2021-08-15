import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass
    
class BinaryNode(Node):
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class NumNode(BinaryNode):
    def __init__(self, val=None, right=None, left=None):
        super().__init__(val, right, left)
    
    def evaluate(self) -> int:
        return int(self.val)

class PlusNode(BinaryNode):
    def __init__(self, val=None, right=None, left=None):
        super().__init__(val, right, left)
    
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

class MinusNode(BinaryNode):
    def __init__(self, val=None, right=None, left=None):
        super().__init__(val, right, left)
    
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class MultiplyNode(BinaryNode):
    def __init__(self, val=None, right=None, left=None):
        super().__init__(val, right, left)
    
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()
    
class DivideNode(BinaryNode):
    def __init__(self, val=None, right=None, left=None):
        super().__init__(val, right, left)
    
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> Node:
        operators = {'+': PlusNode, '-': MinusNode, '*': MultiplyNode, '/': DivideNode}
        stack = []
        for op in postfix:
            if op in operators:
                node = operators[op](op)
                if stack:
                    node.right = stack.pop()
                if stack:
                    node.left = stack.pop()
            else:
                node = NumNode(op)
            stack.append(node)
        return stack[0]
        
                
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        