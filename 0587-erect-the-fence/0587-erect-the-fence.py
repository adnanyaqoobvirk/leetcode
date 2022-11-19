class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        trees.sort()
        
        lower = []
        for x, y in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], (x, y)) < 0:
                lower.pop()
                
            lower.append((x, y))
    
        upper = []
        for x, y in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], (x, y)) < 0:
                upper.pop()
            
            upper.append((x, y))
        
        return  set(lower) | set(upper)
        