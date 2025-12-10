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
        encodes = []
        def encode(curr: TreeNode) -> None:
            if not curr:
                encodes.append("#")
            else:
                encode(curr.right)
                encode(curr.left)
                encodes.append(str(curr.val))
        encode(root)
        return "|".join(encodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        encodes = data.split("|")
        def decode() -> None:
            if not encodes:
                return None
            
            encode = encodes.pop()
            if encode == "#":
                return None

            curr = TreeNode(int(encode))
            curr.left = decode()
            curr.right = decode()
            return curr
        return decode()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))