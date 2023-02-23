# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def int2str(self, num):
        ans = []
        for i in reversed(range(4)):
            ans.append(chr(0xFF & (num >> (8 * i))))
        return "".join(ans)
    
    def str2int(self, s):
        ans = 0
        for c in s:
            ans = ans * 256 + ord(c)
        return ans

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
                
            ans.append(self.int2str(curr.val))
            stack.append(curr.right)
            stack.append(curr.left)
        return "".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data:
            root = TreeNode(self.str2int(data[0:4]))
            stack = [root]
            for i in range(4, len(data), 4):
                curr, child = stack[-1], TreeNode(self.str2int(data[i:i + 4]))
                
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