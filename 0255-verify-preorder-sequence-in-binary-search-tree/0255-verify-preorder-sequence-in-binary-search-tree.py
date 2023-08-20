class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, minlimit = [], -inf
        for v in preorder:
            while stack and stack[-1] < v:
                minlimit = stack.pop()
            if v <= minlimit:
                return False
            stack.append(v)
        return True