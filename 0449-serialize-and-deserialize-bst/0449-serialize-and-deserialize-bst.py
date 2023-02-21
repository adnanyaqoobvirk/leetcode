# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def recurse(curr):
            if not curr:
                ans.append("#")
                return
            
            ans.append(str(curr.val))
            recurse(curr.left)
            recurse(curr.right)
        ans = []
        recurse(root)
        return ",".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def recurse():
            nonlocal pos
            pos += 1
            
            if pos >= n or data[pos] == "#":
                return None
            
            node = TreeNode(int(data[pos]))
            node.left = recurse()
            node.right = recurse()
            return node
        
        data = data.split(",")
        n = len(data)
        pos = -1
        return recurse()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans