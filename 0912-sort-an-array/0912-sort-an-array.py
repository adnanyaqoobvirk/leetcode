class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
    
    def _balance(self, root):
        if not root:
            return 0
        
        return self._height(root.left) - self._height(root.right)
    
    def _height(self, root):
        if not root:
            return 0
        
        return root.height
    
    def _rotateLeft(self, z):
        y = z.right
        x = y.left
        
        y.left = z
        z.right = x
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y
    
    def _rotateRight(self, z):
        y = z.left
        x = y.right
        
        y.right = z
        z.left = x
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y
    
    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        if root.key < key:
            root.right = self._insert(root.right, key)
        elif root.key >= key:
            root.left = self._insert(root.left, key)
        
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        
        b = self._balance(root)
        
        if b > 1:
            if self._balance(root.left) < 0:
                root.left = self._rotateLeft(root.left)
            return self._rotateRight(root)
        elif b < -1:
            if self._balance(root.right) > 0:
                root.right = self._rotateRight(root.right)
            return self._rotateLeft(root)
        
        return root
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def inorder(self):
        ans = []
        if self.root:
            stack = []
            root = self.root
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    curr = stack.pop()
                    ans.append(curr.key)
                    root = curr.right
        return ans
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        t = AVLTree()
        for num in nums:
            t.insert(num)
        return t.inorder()