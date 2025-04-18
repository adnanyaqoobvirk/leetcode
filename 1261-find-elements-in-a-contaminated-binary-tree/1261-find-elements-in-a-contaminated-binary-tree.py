# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.vals = set()
        q = [root]
        while q:
            nq = []
            for node in q:
                self.vals.add(node.val)
                if node.left:
                    node.left.val = node.val * 2 + 1
                    nq.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 2
                    nq.append(node.right)
            q = nq

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)