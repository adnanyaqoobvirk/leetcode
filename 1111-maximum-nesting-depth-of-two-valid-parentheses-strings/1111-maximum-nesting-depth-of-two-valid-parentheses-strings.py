class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        ans = []
        for p in seq:
            if p == '(':
                depth += 1
            
            if depth & 1:
                ans.append(0)
            else:
                ans.append(1)
            
            if p == ')':
                depth -= 1
        return ans