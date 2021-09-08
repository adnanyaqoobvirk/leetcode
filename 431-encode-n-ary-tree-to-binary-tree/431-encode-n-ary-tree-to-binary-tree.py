"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if root:
            node = TreeNode(root.val)
            
            if root.children:
                bchild = None
                for child in root.children:
                    if not bchild:
                        bchild = node.left = self.encode(child)
                    else:
                        bchild.right = self.encode(child)
                        bchild = bchild.right
            return node
                    
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if data:
            node = Node(data.val, [])
            if data.left:
                current = data.left
                while current:
                    node.children.append(self.decode(current))
                    current = current.right
            return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))