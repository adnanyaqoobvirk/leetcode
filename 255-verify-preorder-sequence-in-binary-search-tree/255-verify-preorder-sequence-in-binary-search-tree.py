class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        pos, root = -1, float('-inf')
        for i in range(len(preorder)):
            while pos >= 0 and preorder[pos] < preorder[i]:
                root = preorder[pos]
                pos -= 1
            if preorder[i] < root:
                return False
            pos += 1
            preorder[pos] = preorder[i]
        return True