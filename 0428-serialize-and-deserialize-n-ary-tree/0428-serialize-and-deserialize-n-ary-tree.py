"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        
        ans = [str(root.val), "$"]
        q = [root]
        while q:
            nq = []
            for node in q:
                for child in node.children:
                    ans.append(str(child.val))
                    ans.append(",")
                    nq.append(child)
                if ans[-1] == ",":
                    ans.pop()
                ans.append("|")
            if ans[-1] == "|":
                ans.pop()
            if nq:
                ans.append("$")
            q = nq
        return "".join(ans)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        levels = data.split("$")
        root = Node(int(levels[0]), [])
        q = [root]
        for i in range(1, len(levels)):
            nq = []
            for node, child_vals in zip(q, levels[i].split("|")):
                for child in child_vals.split(","):
                    if child:
                        nq.append(Node(int(child), []))
                        node.children.append(nq[-1])   
            q = nq
        return root
                
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))