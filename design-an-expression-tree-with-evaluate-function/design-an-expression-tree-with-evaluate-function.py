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

class ENode(Node):
    operators = set("+-*/")
    
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
    
    def evaluate(self):
        if self.val not in ENode.operators:
            return int(self.val)
        elif self.left and self.right:
            if self.val == '+':
                return self.left.evaluate() + self.right.evaluate()
            elif self.val == '-':
                return self.left.evaluate() - self.right.evaluate()
            elif self.val == '*':
                return self.left.evaluate() * self.right.evaluate()
            elif self.val == '/':
                return self.left.evaluate() // self.right.evaluate()
        return None
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for op in postfix:
            node = ENode(op)
            if op in ENode.operators:
                if stack:
                    node.right = stack.pop()
                if stack:
                    node.left = stack.pop()
            stack.append(node)
        return stack[0]
        
                
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        