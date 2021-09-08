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
            broot = TreeNode(root.val)
            
            q = [(root, broot)]
            while q:
                nq = []
                for node, bnode in q:
                    if node.children:
                        bchild = None
                        for child in node.children:
                            if not bchild:
                                bnode.left = bchild = TreeNode(child.val)
                            else:
                                bchild.right = TreeNode(child.val)
                                bchild = bchild.right
                            nq.append((child, bchild))
                q = nq
            return broot
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if data:
            root = Node(data.val, [])
            
            q = [(data, root)]
            while q:
                nq = []
                for bnode, node in q:
                    if bnode.left:
                        current = bnode.left
                        while current:
                            child = Node(current.val, [])
                            node.children.append(child)
                            nq.append((current, child))
                            current = current.right
                q = nq
            return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))