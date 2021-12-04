class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, root = [], float('-inf')
        for num in preorder:
            while stack and stack[-1] < num:
                root = stack.pop()
            if num < root:
                return False
            stack.append(num)
        return True