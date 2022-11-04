class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0
        for d in num:
            while stack and stack[-1] > d and removed < k:
                stack.pop()
                removed += 1
            if not stack and d == "0":
                continue
            stack.append(d)
            
        while stack and removed < k:
            stack.pop()
            removed += 1
            
        return "".join(stack) if stack else "0"