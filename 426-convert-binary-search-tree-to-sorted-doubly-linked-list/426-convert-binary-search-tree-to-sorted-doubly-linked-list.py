"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        def helper(curr: Optional[Node]) -> Tuple[Optional[Node], Optional[Node]]:
            if not curr:
                return None, None
            
            left_head, left_tail = helper(curr.left)
            if left_tail:
                left_tail.right, curr.left = curr, left_tail
            
            right_head, right_tail = helper(curr.right)
            if right_tail:
                curr.right, right_head.left = right_head, curr
        
            return left_head if left_head else curr, right_tail if right_tail else curr
        
        head, tail = helper(root)
        head.left, tail.right = tail, head
        return head