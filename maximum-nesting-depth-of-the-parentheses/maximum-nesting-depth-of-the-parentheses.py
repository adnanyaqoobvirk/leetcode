class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            
            if depth > max_depth:
                max_depth = depth
        return max_depth