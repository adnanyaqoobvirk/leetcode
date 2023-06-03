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
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        
        broot = TreeNode(root.val)
        if root.children:
            broot.left = curr = self.encode(root.children[0])
            for i in range(1, len(root.children)):
                curr.right = self.encode(root.children[i])
                curr = curr.right
        return broot
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        
        root = Node(data.val, [])
        if data.left:
            root.children.append(self.decode(data.left))
            curr = data.left.right
            while curr:
                root.children.append(self.decode(curr))
                curr = curr.right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))