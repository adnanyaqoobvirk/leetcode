# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def recurse(curr: Optional[TreeNode]) -> Tuple[int, int, bool, int]:
            if not curr.left and not curr.right:
                return curr.val, curr.val, True, 1
            elif not curr.left:
                rmin, rmax, rvalid, rcount = recurse(curr.right)
                if rvalid and curr.val < rmin:
                    return curr.val, rmax, True, rcount + 1
                else:
                    return inf, -inf, False, 1
            elif not curr.right:
                lmin, lmax, lvalid, lcount = recurse(curr.left)
                if lvalid and lmax < curr.val:
                    return lmin, curr.val, True, lcount + 1
                else:
                    return inf, -inf, False, 1
            else:
                lmin, lmax, lvalid, lcount = recurse(curr.left)
                rmin, rmax, rvalid, rcount = recurse(curr.right)

                if lvalid and rvalid and lmax < curr.val < rmin:
                    return lmin, rmax, True, lcount + rcount + 1
                else:
                    return inf, -inf, False, max(lcount, rcount)
        if not root:
            return 0
        _, _, _, res = recurse(root)
        return res
            