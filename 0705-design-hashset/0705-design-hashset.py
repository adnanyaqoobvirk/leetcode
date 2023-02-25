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
        
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        
        return y
    
    def _rotateRight(self, z):
        y = z.left
        x = y.right
        
        y.right = z
        z.left = x
        
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        
        return y
    
    def _minNode(self, root):
        if not root or not root.left:
            return root
        
        return self._minNode(root.left)
    
    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        if root.key < key:
            root.right = self._insert(root.right, key)
        elif root.key > key:
            root.left = self._insert(root.left, key)
        else:
            return root
        
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
    
    def _delete(self, root, key):
        if not root:
            return None
        
        if root.key < key:
            root.right = self._delete(root.right, key)
        elif root.key > key:
            root.left = self._delete(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.key = self._minNode(root.right).key
                root.right = self._delete(root.right, root.key)
        
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
    
    def _search(self, root, key):
        if not root:
            return False
        
        if root.key < key:
            return self._search(root.right, key)
        
        if root.key > key:
            return self._search(root.left, key)
        
        return True
        
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def search(self, key):
        return self._search(self.root, key)
    
class MyHashSet:

    def __init__(self):
        self.t = AVLTree()

    def add(self, key: int) -> None:
        self.t.insert(key)

    def remove(self, key: int) -> None:
        self.t.delete(key)

    def contains(self, key: int) -> bool:
        return self.t.search(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)