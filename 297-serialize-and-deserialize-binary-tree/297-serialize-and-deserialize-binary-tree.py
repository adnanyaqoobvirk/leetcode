# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(curr):
            if not curr:
                ans.append('#')
            else:
                helper(curr.left)
                helper(curr.right)
                ans.append(str(curr.val))
        ans = []
        helper(root)
        return ",".join(ans)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = arr.pop()
            if val != '#':
                right, left = helper(), helper()
                node = TreeNode(int(val))
                node.left, node.right = left, right
                return node
        
        arr = data.split(",")
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))