# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(lo, hi):
            if lo > hi:
                return None
            
            if lo == hi:
                return nodes[lo]
            
            mid = lo + hi >> 1
            nodes[mid].left = helper(lo, mid - 1)
            nodes[mid].right = helper(mid + 1, hi)
            return nodes[mid]
        
        nodes, curr = [], head
        while curr:
            nodes.append(TreeNode(curr.val))
            curr = curr.next
        return helper(0, len(nodes) - 1)