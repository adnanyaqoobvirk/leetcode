class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        maxDepth = 0
        depth = 0
        for p in seq:
            if p == '(':
                depth += 1
            else:
                depth -= 1
            maxDepth = max(depth, maxDepth)
        
        depth = 0
        ans = []
        for p in seq:
            if p == '(':
                depth += 1
            
            if depth > (maxDepth // 2):
                ans.append(0)
            else:
                ans.append(1)
            
            if p == ')':
                depth -= 1
        return ans