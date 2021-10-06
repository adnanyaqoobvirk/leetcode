# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def getNumDepth(pos: int) -> Tuple[int, int, int]:
            d = 0
            while pos < l and traversal[pos] == '-':
                d += 1
                pos += 1
            
            n = 0
            while pos < l and traversal[pos] != '-':
                n = n * 10 + nmap[traversal[pos]]
                pos += 1
            
            return n, d, pos
        
        nmap = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        l = len(traversal)
        num, depth, tpos = getNumDepth(0)
        stack = [(TreeNode(num), depth)]
        while tpos < l:
            num, depth, tpos = getNumDepth(tpos)
            while stack[-1][1] > depth:
                stack.pop()
            
            if stack[-1][1] == depth:
                stack[-2][0].right = TreeNode(num)
                stack.append((stack[-2][0].right, depth))
            else:
                stack[-1][0].left = TreeNode(num)
                stack.append((stack[-1][0].left, depth))
        
        return stack[0][0]
            