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
        ans = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
                
            ans.append(str(curr.val))
            stack.append(curr.right)
            stack.append(curr.left)
        return ",".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data:
            data = data.split(",")
            root = TreeNode(int(data[0]))
            stack = [root]
            for i in range(1, len(data)):
                curr, child = stack[-1], TreeNode(int(data[i]))
                
                while stack and stack[-1].val < child.val:
                    curr = stack.pop()
                    
                if curr.val < child.val:
                    curr.right = child
                else:
                    curr.left = child
                
                stack.append(child)
            return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans