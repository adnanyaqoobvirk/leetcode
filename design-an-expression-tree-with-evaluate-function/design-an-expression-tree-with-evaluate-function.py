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
    def __init__(self, right=None, left=None):
        self.right = right
        self.left = left

class NumNode(Node):
    def __init__(self, val=None):
        self.val = val
    
    def evaluate(self) -> int:
        return self.val

class PlusNode(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

class MinusNode(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class MultiplyNode(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()
    
class DivideNode(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> Node:
        operators = {'+': PlusNode, '-': MinusNode, '*': MultiplyNode, '/': DivideNode}
        stack = []
        for token in postfix:
            if token in operators:
                node = operators[token](stack.pop(), stack.pop())
            else:
                node = NumNode(int(token))
            stack.append(node)
        return stack[0]
        
                
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        