class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, root = [], None
        for num in preorder:
            while stack and stack[-1] < num:
                root = stack.pop()
            if root and num < root:
                return False
            stack.append(num)
        return True