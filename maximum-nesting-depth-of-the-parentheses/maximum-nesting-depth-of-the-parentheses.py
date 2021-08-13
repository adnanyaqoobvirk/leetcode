class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif c == ')':
                depth -= 1
        return max_depth